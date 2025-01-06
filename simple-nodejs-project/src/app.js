const express = require('express');
const bodyParser = require('body-parser');
const { setAuthRoutes } = require('./routes/authRoutes');
const { setUserRoutes } = require('./routes/userRoutes');

const app = express();
const PORT = process.env.PORT || 3000;

app.use(bodyParser.json());

setAuthRoutes(app);
setUserRoutes(app);

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});