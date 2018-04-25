import React from 'react';
import { Link } from 'react-router-dom';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Menu, { MenuItem } from 'material-ui/Menu';

import Typography from 'material-ui/Typography';
import Avatar from 'material-ui/Avatar';
import MenuIcon from 'material-ui-icons/Menu';
import IconButton from 'material-ui/IconButton';
import Icon from 'material-ui/Icon';

const drawerWidth = 260;

const appBar = {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: drawerWidth,
    backgroundColor: '#1B5E20',
}

const menuButton = {
    marginLeft: 12,
    marginRight: 20,
}


export default class TopHeader extends React.Component {


    render() {
        return (
            <header>
                <AppBar style={appBar}>
                    <Toolbar>
                        <a href="/">
                        <IconButton style={menuButton} color="inherit" aria-label="Menu">
                            <Avatar alt="গনপ্রজাতন্ত্রী বাংলাদেশ" src="/static/images/logo_bdgov.png" />
                        </IconButton>
                        </a>
                        <Typography variant="title" color="inherit" noWrap>
                            <p>দোয়ারা বাজার ভুমি অফিস </p>
                        </Typography>
                        
                    </Toolbar>
                </AppBar>
            </header>
        );
    }
}
