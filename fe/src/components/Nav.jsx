import React from 'react';
import {IndexLink} from 'react-router';

var activeStyle = {
    fontWeight: 'bold'
};
class LogInOut extends React.Component {
    render() {
        if (this.props.validSession) {
            return (
                <li>
                    <IndexLink activeClassName="active" activeStyle={activeStyle} to="/logout">Logout</IndexLink>
                </li>
            );
        } else {
            return (
                <li>
                    <IndexLink activeClassName="active" activeStyle={activeStyle} to="/login">Login</IndexLink>
                </li>
            );
        }
    }
}

export default class Nav extends React.Component {
    render() {
        return (
            <div className="top-bar">
                <div className="row">
                    <div className="top-bar-left">
                        <ul className="menu">
                            <li className="menu-text">Lambda OJ v2</li>
                        </ul>
                    </div>

                    <div className="top-bar-right">
                        <ul className="dropdown menu" data-dropdown-menu id={this.props.componentId || 'nav'}>
                            <li>
                                <IndexLink activeClassName="active" activeStyle={activeStyle} to="/">Home</IndexLink>
                            </li>
                            <li>
                                <IndexLink activeClassName="active" activeStyle={activeStyle} to="/oj">Online Judge</IndexLink>
                                <ul className="menu">
                                    <li>
                                        <IndexLink activeClassName="active" activeStyle={activeStyle} to="oj">Problems</IndexLink>
                                    </li>
                                    <li>
                                        <IndexLink activeClassName="active" activeStyle={activeStyle} to="oj/submit">Submit</IndexLink>
                                    </li>
                                    <li>
                                        <IndexLink activeClassName="active" activeStyle={activeStyle} to="oj/status">Status</IndexLink>
                                    </li>
                                    <li>
                                        <IndexLink activeClassName="active" activeStyle={activeStyle} to="oj/profile">Profile</IndexLink>
                                    </li>
                                </ul>
                            </li>
                            <LogInOut validSession={false}/>
                        </ul>
                    </div>
                </div>
            </div>
        );
    }
}
