const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 5000;

// Middleware
app.use(bodyParser.json());
app.use(cors());

// In-memory database (for demonstration purposes)
let audits = [];

// Fetch audits
app.get('/api/audits', (req, res) => {
    res.json(audits);
});

// Add a new audit
app.post('/api/audits', (req, res) => {
    const newAudit = req.body;
    newAudit.audit_date = new Date().toISOString();
    audits.push(newAudit);
    res.status(201).json(newAudit);
});

// Start the server
app.listen(port, () => {
    console.log(`Server is running on http://127.0.0.1:${port}`);
});