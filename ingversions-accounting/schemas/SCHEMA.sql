-- ingversions digital - Accounting System Database Schema
-- Compatible with PostgreSQL and SQLite

-- Drop tables if they exist (for clean setup)
DROP TABLE IF EXISTS document_logs;
DROP TABLE IF EXISTS form16_details;
DROP TABLE IF EXISTS expense_items;
DROP TABLE IF EXISTS expenses;
DROP TABLE IF EXISTS salary_records;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS clients;
DROP TABLE IF EXISTS tax_slabs;

-- Clients table for revenue/profit tracking
CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    client_code VARCHAR(20) UNIQUE NOT NULL,
    client_name VARCHAR(200) NOT NULL,
    contact_person VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(20),
    address TEXT,
    contract_value DECIMAL(15,2) DEFAULT 0,
    gst_number VARCHAR(20),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Employees master table
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    employee_id VARCHAR(20) UNIQUE NOT NULL,
    full_name VARCHAR(100) NOT NULL,
    designation VARCHAR(50) NOT NULL,
    department VARCHAR(50),
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_joining DATE NOT NULL,
    date_of_birth DATE,
    pan_number VARCHAR(10),
    aadhar_number VARCHAR(12),
    bank_name VARCHAR(100),
    bank_account VARCHAR(20),
    ifsc_code VARCHAR(11),
    epf_uan VARCHAR(20),
    esic_number VARCHAR(20),
    ctc_annual DECIMAL(12,2) NOT NULL,
    basic_salary DECIMAL(12,2),
    hra DECIMAL(12,2),
    conveyance DECIMAL(10,2) DEFAULT 0,
    medical DECIMAL(10,2) DEFAULT 0,
    special_allowance DECIMAL(12,2) DEFAULT 0,
    team_id VARCHAR(50), -- Microsoft Teams user ID
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Monthly attendance tracking
CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    employee_id VARCHAR(20) NOT NULL,
    year_month VARCHAR(7) NOT NULL, -- Format: YYYY-MM
    month_name VARCHAR(10) NOT NULL,
    total_days_in_month INTEGER NOT NULL,
    working_days INTEGER NOT NULL,
    days_present INTEGER DEFAULT 0,
    days_absent INTEGER DEFAULT 0,
    days_leave INTEGER DEFAULT 0,
    days_weekoff INTEGER DEFAULT 0,
    days_half_day INTEGER DEFAULT 0,
    lop_days DECIMAL(5,2) DEFAULT 0,
    paid_days DECIMAL(5,2) DEFAULT 0,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    UNIQUE(employee_id, year_month)
);

-- Monthly salary records with calculation breakdown
CREATE TABLE salary_records (
    id SERIAL PRIMARY KEY,
    employee_id VARCHAR(20) NOT NULL,
    year_month VARCHAR(7) NOT NULL,
    month_name VARCHAR(10) NOT NULL,
    
    -- Earnings
    basic_salary DECIMAL(12,2) NOT NULL,
    hra DECIMAL(12,2) DEFAULT 0,
    conveyance_allowance DECIMAL(12,2) DEFAULT 0,
    medical_allowance DECIMAL(12,2) DEFAULT 0,
    special_allowance DECIMAL(12,2) DEFAULT 0,
    overtime DECIMAL(10,2) DEFAULT 0,
    bonus DECIMAL(10,2) DEFAULT 0,
    other_earnings DECIMAL(10,2) DEFAULT 0,
    gross_earnings DECIMAL(12,2) NOT NULL,
    
    -- Deductions
    pf_employee DECIMAL(10,2) DEFAULT 0,
    esi_employee DECIMAL(10,2) DEFAULT 0,
    tds DECIMAL(10,2) DEFAULT 0,
    professional_tax DECIMAL(8,2) DEFAULT 0,
    advance_deduction DECIMAL(10,2) DEFAULT 0,
    other_deductions DECIMAL(10,2) DEFAULT 0,
    total_deductions DECIMAL(12,2) NOT NULL,
    
    -- Net
    net_salary DECIMAL(12,2) NOT NULL,
    
    -- Employer contributions
    pf_employer DECIMAL(10,2) DEFAULT 0,
    esi_employer DECIMAL(10,2) DEFAULT 0,
    
    -- Payment info
    payment_mode VARCHAR(20) DEFAULT 'Bank Transfer',
    payment_date DATE,
    payment_status VARCHAR(20) DEFAULT 'Pending',
    payslip_generated BOOLEAN DEFAULT FALSE,
    payslip_path VARCHAR(255),
    
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    UNIQUE(employee_id, year_month)
);

-- Expense categories
CREATE TABLE expense_categories (
    id SERIAL PRIMARY KEY,
    category_code VARCHAR(20) UNIQUE NOT NULL,
    category_name VARCHAR(50) NOT NULL,
    is_billable BOOLEAN DEFAULT TRUE,
    is_reimbursable BOOLEAN DEFAULT TRUE
);

-- Expense headers
CREATE TABLE expenses (
    id SERIAL PRIMARY KEY,
    expense_date DATE NOT NULL,
    employee_id VARCHAR(20) NOT NULL,
    client_id INTEGER,
    expense_number VARCHAR(30) UNIQUE NOT NULL,
    category VARCHAR(50) NOT NULL,
    description TEXT,
    amount DECIMAL(12,2) NOT NULL,
    currency VARCHAR(3) DEFAULT 'INR',
    gst_amount DECIMAL(10,2) DEFAULT 0,
    total_amount DECIMAL(12,2) NOT NULL,
    receipt_attached BOOLEAN DEFAULT FALSE,
    receipt_path VARCHAR(255),
    project_code VARCHAR(20),
    approved_by VARCHAR(50),
    approval_date DATE,
    status VARCHAR(20) DEFAULT 'Pending', -- Pending, Approved, Rejected, Reimbursed
    reimbursement_date DATE,
    team_notification_sent BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    FOREIGN KEY (client_id) REFERENCES clients(id)
);

-- Form 16 data (Annual tax certificate)
CREATE TABLE form16_data (
    id SERIAL PRIMARY KEY,
    employee_id VARCHAR(20) NOT NULL,
    financial_year VARCHAR(9) NOT NULL, -- Format: YYYY-YYYY
    assessment_year VARCHAR(9) NOT NULL,
    
    -- Part A (TRACES/Employer)
    employer_name VARCHAR(200) DEFAULT 'ingversions digital',
    employer_tan VARCHAR(10),
    employer_pan VARCHAR(10),
    
    -- Income details
    gross_salary DECIMAL(12,2) DEFAULT 0,
    exempt_allowances DECIMAL(10,2) DEFAULT 0,
    balance_income DECIMAL(12,2) DEFAULT 0,
    deductions_std DECIMAL(10,2) DEFAULT 50000, -- Standard deduction
    chapter_vi_a DECIMAL(10,2) DEFAULT 0, -- 80C, 80D, etc.
    taxable_income DECIMAL(12,2) DEFAULT 0,
    tax_on_income DECIMAL(10,2) DEFAULT 0,
    rebate_87a DECIMAL(10,2) DEFAULT 0,
    tax_after_rebate DECIMAL(10,2) DEFAULT 0,
    cess_4 DECIMAL(8,2) DEFAULT 0,
    total_tax DECIMAL(10,2) DEFAULT 0,
    
    -- Tax deducted
    total_tds_deducted DECIMAL(10,2) DEFAULT 0,
    tax_payable_refund DECIMAL(10,2) DEFAULT 0,
    
    -- Form 16 generation
    form16_generated BOOLEAN DEFAULT FALSE,
    form16_path VARCHAR(255),
    generation_date TIMESTAMP,
    sent_to_employee BOOLEAN DEFAULT FALSE,
    sent_date TIMESTAMP,
    
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id),
    UNIQUE(employee_id, financial_year)
);

-- Document generation log (audit trail)
CREATE TABLE document_logs (
    id SERIAL PRIMARY KEY,
    document_type VARCHAR(30) NOT NULL, -- Payslip, Form16, Report, etc.
    reference_id INTEGER NOT NULL,
    employee_id VARCHAR(20),
    document_name VARCHAR(100) NOT NULL,
    file_path VARCHAR(255),
    file_size INTEGER,
    generated_by VARCHAR(50) DEFAULT 'n8n',
    generated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    sent_via VARCHAR(20), -- Email, Teams, Download
    recipient_teams_id VARCHAR(50),
    status VARCHAR(20) DEFAULT 'Generated',
    error_message TEXT
);

-- Monthly financial summary (for reports)
CREATE TABLE monthly_financial_summary (
    id SERIAL PRIMARY KEY,
    year_month VARCHAR(7) NOT NULL,
    month_name VARCHAR(10) NOT NULL,
    
    -- Revenue
    total_revenue DECIMAL(15,2) DEFAULT 0,
    client_revenue JSONB,
    
    -- Expenses
    total_expenses DECIMAL(15,2) DEFAULT 0,
    salary_expenses DECIMAL(15,2) DEFAULT 0,
    operating_expenses DECIMAL(15,2) DEFAULT 0,
    client_expenses JSONB,
    category_expenses JSONB,
    
    -- Summary
    gross_profit DECIMAL(15,2) DEFAULT 0,
    net_profit DECIMAL(15,2) DEFAULT 0,
    profit_margin DECIMAL(5,2) DEFAULT 0,
    
    report_generated BOOLEAN DEFAULT FALSE,
    report_path VARCHAR(255),
    sent_to_teams BOOLEAN DEFAULT FALSE,
    sent_date TIMESTAMP,
    
    UNIQUE(year_month)
);

-- India Tax Slabs (FY 2024-25 - Old Regime)
CREATE TABLE tax_slabs (
    id SERIAL PRIMARY KEY,
    regime VARCHAR(10) NOT NULL, -- old, new
    slab_min DECIMAL(12,2) NOT NULL,
    slab_max DECIMAL(12,2), -- NULL for above
    tax_rate DECIMAL(5,2) NOT NULL,
    cess_applicable BOOLEAN DEFAULT TRUE
);

-- Insert default expense categories
INSERT INTO expense_categories (category_code, category_name, is_billable, is_reimbursable) VALUES
('TRAVEL', 'Travel & Transportation', TRUE, TRUE),
('MEALS', 'Meals & Entertainment', TRUE, TRUE),
('OFFICE', 'Office Supplies', FALSE, TRUE),
('HARDWARE', 'Hardware & Equipment', FALSE, TRUE),
('SOFTWARE', 'Software & Subscriptions', FALSE, TRUE),
('COMM', 'Communication & Internet', FALSE, TRUE),
('TRAINING', 'Training & Development', FALSE, TRUE),
('MARKETING', 'Marketing & Advertising', FALSE, TRUE),
('UTILITIES', 'Utilities & Rent', FALSE, TRUE),
('MISC', 'Miscellaneous', TRUE, TRUE);

-- Insert tax slabs for FY 2024-25 (Old Regime)
INSERT INTO tax_slabs (regime, slab_min, slab_max, tax_rate) VALUES
('old', 0, 250000, 0),
('old', 250000, 500000, 5),
('old', 500000, 1000000, 20),
('old', 1000000, NULL, 30);

-- Create indexes for performance
CREATE INDEX idx_employees_active ON employees(is_active);
CREATE INDEX idx_salary_yearmonth ON salary_records(year_month);
CREATE INDEX idx_attendance_yearmonth ON attendance(year_month);
CREATE INDEX idx_expenses_date ON expenses(expense_date);
CREATE INDEX idx_expenses_client ON expenses(client_id);
CREATE INDEX idx_expenses_status ON expenses(status);
CREATE INDEX idx_form16_fy ON form16_data(financial_year);

-- Views
-- Active employees with current month salary
CREATE VIEW vw_employee_salary_summary AS
SELECT 
    e.employee_id,
    e.full_name,
    e.designation,
    e.department,
    e.email,
    e.is_active,
    e.ctc_annual,
    s.year_month,
    s.gross_earnings,
    s.total_deductions,
    s.net_salary,
    s.payment_status,
    s.payslip_generated
FROM employees e
LEFT JOIN salary_records s ON e.employee_id = s.employee_id
    AND s.year_month = TO_CHAR(CURRENT_DATE, 'YYYY-MM')
WHERE e.is_active = TRUE;

-- Monthly expense summary by client
CREATE VIEW vw_client_expense_summary AS
SELECT 
    c.id AS client_id,
    c.client_name,
    c.client_code,
    TO_CHAR(e.expense_date, 'YYYY-MM') AS year_month,
    SUM(e.amount) AS total_expenses,
    SUM(e.total_amount) AS total_with_gst,
    COUNT(*) AS expense_count
FROM clients c
LEFT JOIN expenses e ON c.id = e.client_id
GROUP BY c.id, c.client_name, c.client_code, TO_CHAR(e.expense_date, 'YYYY-MM');

-- Trigger for updating timestamp
CREATE OR REPLACE FUNCTION update_modified_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_employees_modtime 
    BEFORE UPDATE ON employees 
    FOR EACH ROW 
    EXECUTE FUNCTION update_modified_column();

CREATE TRIGGER update_clients_modtime 
    BEFORE UPDATE ON clients 
    FOR EACH ROW 
    EXECUTE FUNCTION update_modified_column();