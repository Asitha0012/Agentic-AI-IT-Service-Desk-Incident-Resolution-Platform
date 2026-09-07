CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL CHECK (role IN ('employee', 'agent','manager', 'admin'))
);

CREATE TABLE IF NOT EXISTS assets (
    id SERIAL PRIMARY KEY,
    asset_tag TEXT UNIQUE NOT NULL,
    owner_username TEXT NOT NULL,
    asset_type TEXT NOT NULL,
    os_name TEXT,
    health_score NUMERIC(5,2) DEFAULT 100,
    warranty_end DATE,
    status TEXT NOT NULL DEFAULT 'active'
);

CREATE TABLE IF NOT EXISTS tickets (
    id SERIAL PRIMARY KEY,
    requester TEXT NOT NULL,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT,
    priority TEXT NOT NULL DEFAULT 'P3',
    status TEXT NOT NULL DEFAULT 'open',
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS approvals (
    id SERIAL PRIMARY KEY,
    ticket_id INTEGER REFERENCES tickets(id),
    action TEXT NOT NULL,
    risk_level TEXT NOT NULL,
    reason TEXT,
    status TEXT NOT NULL DEFAULT 'pending',
    requested_by TEXT,
    reviewed_by TEXT,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    reviewed_at TIMESTAMPTZ
);

CREATE TABLE IF NOT EXISTS audit_log (
    id BIGSERIAL PRIMARY KEY,
    actor TEXT,
    action TEXT NOT NULL,
    resource_type TEXT,
    resource_id TEXT,
    decision TEXT,
    metadata JSONB,
    created_at TIMESTAMPTZ DEFAULT NOW()
);

INSERT INTO users(username, role) VALUES
    ('alice','employee'), ('bob','agent'), ('carol', 'manager'), ('david', 'admin')
ON CONFLICT DO NOTHING;

INSERT INTO assets(asset_tag, owner_username, asset_type, os_name, health_score, status) 
VALUES
    ('LT-1001','alice', 'laptop', 'Windows 11', 94, 'active'),
    ('LT-1002', 'bob', 'laptop', 'Windows 11', 72, 'active'),
    ('SRV-2001','platform','server', 'Ubuntu 24.04', 61, 'active')
ON CONFLICT DO NOTHING;