import React from 'react';
import {render} from 'react-dom';
import {Router, Route, hashHistory, IndexRoute} from 'react-router';

import Home from 'Home';
import OnlineJudge from 'OnlineJudge';
import Login from 'Login';
import Main from 'Main';

import Problems from 'oj/Problems';
import Submit from 'oj/Submit';
import Status from 'oj/Status';
import Profile from 'oj/Profile';

require('foundation.min.css');
require('main.less');
// require('foundation.min.js');
 // path="problems"
render(
    <Router history={hashHistory}>
        <Route path="/" component={Main}>
            <IndexRoute component={Home}/>
            <Route path="oj" component={OnlineJudge}>
                <IndexRoute component={Problems}></IndexRoute>
                <Route path="submit" component={Submit}></Route>
                <Route path="status" component={Status}></Route>
                <Route path="profile" component={Profile}></Route>
            </Route>
            <Route path="login" component={Login}/>
        </Route>
    </Router>, document.getElementById('app'));
