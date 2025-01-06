function setUserRoutes(app) {
    const userController = require('../controllers/userController');
    const userCtrl = new userController.UserController();

    app.get('/user', (req, res) => {
        const userData = userCtrl.getUserData();
        res.json(userData);
    });
}

module.exports = { setUserRoutes };