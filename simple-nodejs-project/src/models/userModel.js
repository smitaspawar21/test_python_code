class UserModel {
    constructor() {
        this.users = [
            { username: 'john_doe', password: 'password123', name: 'John Doe', email: 'john@example.com', mobile: '123-456-7890' },
            { username: 'jane_doe', password: 'password456', name: 'Jane Doe', email: 'jane@example.com', mobile: '987-654-3210' }
        ];
    }

    findUserByUsername(username) {
        return this.users.find(user => user.username === username);
    }

    getUserData(username) {
        const user = this.findUserByUsername(username);
        if (user) {
            const { name, email, mobile } = user;
            return { name, email, mobile };
        }
        return null;
    }
}

module.exports = UserModel;