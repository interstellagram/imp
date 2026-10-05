function login(username, password) {
    console.log("Logging in:", username);
    console.log("Password:", password);

    return {
        username,
        authenticated: true
    };
}

module.exports = { login };