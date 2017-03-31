import React from 'react';
import Nav from 'Nav';

export default class Main extends React.Component {
    constructor(props) {
        super(props);
    }
    render() {
        return (
            <div id="main">
                <Nav/>
                <div className="content row">
                    {this.props.children}
                </div>
            </div>
        );
    }
}
