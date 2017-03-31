import React from 'react';

export default class Login extends React.Component {
    render() {
        return (
            <div className="logPage row">
                <div className="blured">
                    <form onSubmit={this.handleSubmit} className="small-12 large-4 large-offset-4 columns">
                        <h2>Log in</h2>
                        <div className="bg"></div>
                        <input type="text" ref="userName" placeholder="Enter user name"/>
                        <input type="password" ref="password" placeholder="Enter password"/>
                        <p className="help-text" id="passwordHelpText">Your password must have at least 10 characters, a number, and an Emoji.</p>
                        <input type="text" ref="studentId" placeholder="Enter student id"/>
                        <label htmlFor="remember" ref="remember">
                            <input id="remember" type="checkbox"/>
                            Remember me</label>
                        <button className="button success expanded">Sign in</button>
                        <a className="button small right warning">Register</a>
                    </form>
                </div>
            </div>
        );
    }
    handleSubmit(e) {
        e.preventDefault();
        if (this.validateInput()) {
            //TODO
        }
    }
    validateInput() {
        return true;
    }
}
