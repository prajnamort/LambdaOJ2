import React from 'react';
import {Link} from 'react-router';

class Pro extends React.Component {
    render() {
        return (
            <div className="problemItem">
                <Link to={`oj/submit/${this.props.sn || '#'}`}>
                    <span className="sn">{this.props.sn || '#'}</span>
                    {this.props.name}
                </Link>
            </div>
        );
    }
}

export default class Problems extends React.Component {
    render() {
        return (
            <div className="row">
                <div className="problemsPage small-12 large-10 large-offset-1 columns">
                    <h1>Problems</h1>
                    <Pro sn="1" name="实验十： 骰子日历"/>
                    <Pro sn="2" name="实验九：最大子数组问题"/>
                    <Pro name="实验八：超定方程组的求解"/>
                    <Pro name="实验七：序列求和问题"/>
                    <Pro name="实验六：生成英文回文串"/>

                    <Pro sn="102455" name="实验六：生成英文回文串"/>
                    <Pro sn="102455" name="实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串实验六：生成英文回文串"/>
                </div>
            </div>
        );
    }
}
