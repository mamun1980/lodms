import React from 'react';
import { render } from 'react-dom';

// import { Header } from './components/header';
// import { Home } from './home';

import Drawer from 'material-ui/Drawer';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import IconButton from 'material-ui/IconButton';
import MenuIcon from 'material-ui-icons/Menu';
import Button from 'material-ui/Button';

class CasemsApp extends React.Component {
    constructor() {
        super();
    }

    render() {
        return (
            <div>
                hello
            </div>
        );
    }
}

render(<CasemsApp />, document.querySelector('#casems_home'));
