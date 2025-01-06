function setAuthRoutes(app) {
    const authController = require('../controllers/authController');
    const controller = new authController.AuthController();

    app.post('/login', (req, res) => {
        const { username, password } = req.body;
        controller.login(username, password)
            .then(token => res.json({ token }))
            .catch(err => res.status(401).json({ error: err.message }));
    });
}

module.exports = setAuthRoutes;