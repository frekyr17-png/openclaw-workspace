# Figma MCP Knowledge Base - Phase 1

## MCP Protocol Fundamentals

### What is MCP?
Model Context Protocol (MCP) enables AI agents to interact with external tools/resources via standardized interface. Inspired by Claude Computer Use patterns.

### MCP Core Concepts
- **Resources**: Data sources (Figma files, components, styles)
- **Tools**: Actions (create node, update style, export asset)
- **Prompts**: Templates for common workflows
- **Server**: Figma MCP server implementing the protocol

## Figma REST API Endpoints

### Authentication
```
Header: X-Figma-Token: {access_token}
Base URL: https://api.figma.com/v1
```

### Core Endpoints

**Files**
- `GET /files/:key` - Get file content
- `GET /files/:key/nodes` - Get specific nodes
- `GET /files/:key/images` - Export images from file

**Projects**
- `GET /projects/:project_id/files` - List project files
- `GET /teams/:team_id/projects` - List team projects

**Components**
- `GET /files/:key/components` - Get file components
- `GET /teams/:team_id/components` - Get team components
- `POST /components/:component_id/instances` - Create instance

**Styles**
- `GET /files/:key/styles` - Get file styles
- `GET /teams/:team_id/styles` - Get team styles

**Comments**
- `GET /files/:key/comments` - Get comments
- `POST /files/:key/comments` - Add comment
- `DELETE /files/:key/comments/:comment_id`

**Webhooks**
- `POST /webhooks` - Subscribe to events
- `GET /webhooks` - List webhooks
- `DELETE /webhooks/:id` - Unsubscribe

### File Structure (JSON Response)
```json
{
  "document": {
    "id": "0:0",
    "name": "Document",
    "type": "DOCUMENT",
    "children": [{
      "id": "1:2",
      "name": "Page 1",
      "type": "CANVAS",
      "children": [
        {"id": "2:3", "name": "Frame 1", "type": "FRAME"}
      ]
    }]
  },
  "components": {},
  "componentSets": {},
  "schemaVersion": 0,
  "styles": {}
}
```

## Node Types
- `DOCUMENT` - Root container
- `CANVAS` - Page
- `FRAME` / `GROUP` - Layout containers
- `RECTANGLE`, `ELLIPSE`, `POLYGON`, `STAR`, `VECTOR` - Shapes
- `TEXT` - Text elements
- `COMPONENT` / `COMPONENT_SET` / `INSTANCE` - Component system
- `SLICE` - Exportable areas

## Design Tokens Mapping

### Colors → Design Tokens
```json
{
  "color": {
    "primary": {#000000FF}
    "secondary": {#FFFFFF00}
  }
}
```

### Typography → Design Tokens
```json
{
  "fontSize": {"base": 16, "lg": 18},
  "fontFamily": {"sans": "Inter"},
  "lineHeight": {"normal": 1.5}
}
```

### Spacing → Design Tokens
```json
{
  "spacing": {"xs": 4, "sm": 8, "md": 16, "lg": 24}
}
```

## Advanced Patterns

### Real-Time Sync Workflow
1. Webhook → File change event
2. MCP server fetches updated file
3. Diff against cached version
4. Trigger downstream updates (tokens, components)

### Asset Management Pipeline
1. Detect exportable nodes (SLICE, export settings)
2. Request image exports (PNG, SVG, PDF)
3. Transform/optimize assets
4. Sync to CDN/storage

### Design System Automation
1. Scan components for changes
2. Update documentation
3. Publish to registry
4. Notify consumers (Discord, Slack)

### Team Collaboration Features
1. Comment aggregation
2. Review status tracking
3. Approval workflows
4. Version diffing

## MCP Tool Design for Figma

```typescript
// Example MCP server structure
interface FigmaMCPServer {
  // Resources
  "figma://file/{key}": FigmaFile;
  "figma://component/{id}": FigmaComponent;
  
  // Tools
  "figma_get_file": (key: string) => FigmaFile;
  "figma_export_image": (key: string, nodeId: string) => Buffer;
  "figma_get_components": (key: string) => Component[];
  "figma_update_component": (key: string, id: string, updates: Partial) => Result;
}
```

## Integration Scenarios

### Figma → N8N Workflows
- Webhook trigger on file update
- Extract design tokens
- Send to Slack/Discord
- Update Notion documentation
- Trigger CI/CD pipeline

### Figma → Design Tokens → Code
```mermaid
Figma File → Extract Styles → JSON Tokens → Style Dictionary → CSS/Tailwind/SCSS
```

### Figma → Component Library Generation
```
Figma Components → Parse Properties → Generate Props Interface → Output React/Vue Component
```

### Multi-File Batch Operations
1. Fetch all files in project
2. Extract common design tokens
3. Normalize variations
4. Generate consolidated tokens JSON
5. Compare across files for consistency

## Phase 1 Deliverables Checklist
- [x] MCP protocol understanding
- [x] Figma API endpoint reference
- [x] Node type mapping
- [x] Design tokens structure
- [x] Integration patterns documented
