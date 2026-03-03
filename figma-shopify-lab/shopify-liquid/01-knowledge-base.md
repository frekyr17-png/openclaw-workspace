# Shopify Liquid Knowledge Base - Phase 1

## Liquid Template Language Fundamentals

### Liquid Syntax Types

**Objects** - Output data
```liquid
{{ product.title }}
{{ customer.name | upcase }}
{{ cart.total_price | money }}
```

**Tags** - Logic and control flow
```liquid
{% if product.available %}
  Add to Cart
{% endif %}

{% for variant in product.variants %}
  {{ variant.title }}
{% endfor %}

{% assign color = 'red' %}
{% capture description %}
  This is a {{ product.type }}
{% endcapture %}
```

**Filters** - Transform output
```liquid
{{ product.title | upcase }}
{{ product.price | money }}
{{ product.description | truncate: 100 }}
{{ 'image.jpg' | asset_url }}
{{ product.tags | join: ', ' }}
```

## Theme Architecture

### Directory Structure
```
theme/
├── assets/          # Images, CSS, JS, fonts
├── config/          # Settings_schema.json, settings_data.json
├── layout/          # theme.liquid (main layout)
├── locales/         # Translation files (en.default.json)
├── sections/        # Theme sections (header.liquid, footer.liquid)
├── snippets/        # Reusable code chunks
├── templates/       # Page templates
│   ├── product.liquid
│   ├── collection.liquid
│   ├── cart.liquid
│   ├── page.liquid
│   ├── article.liquid
│   └── customers/
└── templates/customers/  # Account pages
```

### Sections (v2.0+)
Self-contained modular blocks with schema
```liquid
{% schema %}
{
  "name": "Hero Banner",
  "class": "hero-section",
  "settings": [
    {
      "type": "image_picker",
      "id": "background_image",
      "label": "Background Image"
    },
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Welcome"
    }
  ],
  "blocks": [
    {
      "type": "slide",
      "name": "Slide",
      "settings": [
        {"type": "image_picker", "id": "image", "label": "Image"}
      ]
    }
  ],
  "presets": [
    {"name": "Hero Banner", "category": "Image"}
  ]
}
{% endschema %}

{{ section.settings.heading }}
```

### Blocks
Reusable elements within sections
```liquid
{% for block in section.blocks %}
  {% case block.type %}
    {% when 'text' %}
      <p>{{ block.settings.text }}</p>
    {% when 'image' %}
      <img src="{{ block.settings.image | img_url: 'large' }}">
  {% endcase %}
{% endfor %}
```

### Snippets
Reusable components, included with parameters
```liquid
<!-- snippets/product-card.liquid -->
<a href="{{ product.url }}">
  <img src="{{ product.featured_image | img_url: 'medium' }}">
  <h3>{{ product.title }}</h3>
  <p>{{ product.price | money }}</p>
</a>

<!-- Usage -->
{% render 'product-card', product: featured_product %}
```

## Core Liquid Objects

### Global Objects
- `shop` - Shop information
- `cart` - Current cart
- `customer` - Logged-in customer
- `template` - Current template name
- `page_title`, `page_description` - SEO

### Product
```liquid
{{ product.title }}
{{ product.price | money }}
{{ product.compare_at_price | money }}
{{ product.featured_image | img_url: 'large' }}
{{ product.description }}
{{ product.available }}
{{ product.variants }}
{{ product.options }}
{{ product.metafields.custom.field }}
```

### Collection
```liquid
{{ collection.title }}
{{ collection.description }}
{{ collection.all_products_count }}
{{ collection.products | where: "available", true }}
{{ collection.image | img_url: 'large' }}
{% for product in collection.products limit: 20 %}
  {% render 'product-card', product: product %}
{% endfor %}
```

### Cart
```liquid
{{ cart.item_count }}
{{ cart.total_price | money }}
{% for item in cart.items %}
  {{ item.quantity }} x {{ item.product.title }}
{% endfor %}
```

## Liquid Filters Reference

### String
- `upcase`, `downcase`, `capitalize`
- `strip_html`, `truncate`, `truncatewords`
- `replace`, `remove`, `split`, `join`
- `handleize` → URL-friendly string

### Number
- `plus`, `minus`, `times`, `divided_by`, `modulo`
- `money`, `money_with_currency`
- `round`, `ceil`, `floor`

### Date
- `date: '%Y-%m-%d'` - Format dates
- `time_tag` - HTML time element

### HTML/URL
- `link_to`, `link_to_tag`
- `img_url: 'size'` - e.g., 'thumb', 'medium', 'large', '1024x1024'
- `asset_url`, `img_url`, `file_url`
- `within: collection` - Collection-scoped link

### Array
- `first`, `last`, `size`
- `sort`, `where`, `map`
- `compact`, `uniq`, `reverse`

## Advanced Techniques

### Performance Optimization
```liquid
<!-- Lazy loading images -->
<img loading="lazy" src="{{ image | img_url: '600x' }}">

<!-- Preconnect to CDN -->
<link rel="preconnect" href="https://cdn.shopify.com">

<!-- Minimize render-blocking -->
{{ 'theme.css' | asset_url | stylesheet_tag: preload: true }}
```

### Metafields (v2.0+)
```liquid
{{ product.metafields.custom.ingredients }}
{{ collection.metafields.custom.banner_text }}
{{ customer.metafields.custom.loyalty_points }}
```

### Ajax/API Requests (JavaScript)
```javascript
// Add to cart via Ajax
fetch('/cart/add.js', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify({id: variantId, quantity: 1})
})
```

### Custom App Integration
```liquid
{% assign recommendation = recommendations.products.first %}
<div data-product-handle="{{ product.handle }}" class="recommendation-wrapper"></div>

<script>
  // App injects data here
  window.productData = {{ product | json }};
</script>
```

## Real-World Scenarios

### Multi-Currency
```liquid
{% assign currency = cart.currency.iso_code %}
{{ product.price | money_with_currency }}
```

### Subscription Products
```liquid
{% if product.tags contains 'subscription' %}
  <div class="subscription-options">
    <!-- Recharge/Subbly integration -->
  </div>
{% endif %}
```

### Dynamic Pricing
```liquid
{% assign discount = customer.tags | where: 'vip' | size | times: 10 %}
{% assign discounted_price = product.price | times: discount | divided_by: 100 %}
{% assign final_price = product.price | minus: discounted_price %}
{{ final_price | money }}
```

### Personalization Engine
```liquid
{% assign recently_viewed = customer.metafields.custom.recently_viewed | split: ',' %}
{% for handle in recently_viewed limit: 4 %}
  {% assign product = all_products[handle] %}
  {% render 'product-card', product: product %}
{% endfor %}
```

## Phase 1 Deliverables Checklist
- [x] Liquid syntax (objects, tags, filters)
- [x] Theme architecture (sections, blocks, snippets)
- [ ] Asset pipeline (detailed)
- [x] Metafields integration
- [ ] Performance optimization (detailed)
- [ ] Custom apps integration (detailed)
- [x] Real-world scenario patterns
