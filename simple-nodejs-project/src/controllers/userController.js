class UserController {
    getUserData(req, res) {
        // Sample user data
        const userData = {
            name: "John Doe",
            email: "john.doe@example.com",
            mobile: "+1234567890"
        };

        res.json(userData);
    }
}

module.exports = UserController;