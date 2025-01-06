class AuthController {
    constructor(userModel) {
        this.userModel = userModel;
    }

    async login(username, password) {
        const user = await this.userModel.findUserByUsername(username);
        if (user && user.password === password) {
            return { success: true, message: 'Login successful', user: { name: user.name, email: user.email, mobile: user.mobile } };
        }
        return { success: false, message: 'Invalid username or password' };
    }
}

module.exports = AuthController;