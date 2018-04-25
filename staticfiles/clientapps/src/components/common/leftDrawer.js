import React from 'react';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

import PropTypes from 'prop-types';

import Drawer from 'material-ui/Drawer';
import Divider from 'material-ui/Divider';
import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import { withStyles } from 'material-ui/styles';
import Avatar from 'material-ui/Avatar';


import MenuIcon from 'material-ui-icons/Menu';
import IconButton from 'material-ui/IconButton';
import PhotoCamera from 'material-ui-icons/PhotoCamera';
import DraftsIcon from 'material-ui-icons/Drafts';
import SendIcon from 'material-ui-icons/Send';
import StarBorder from 'material-ui-icons/StarBorder';


import LeftMenu from './leftMenu';


const drawerWidth = 260;

const styles = {

    drawerPaper: {
        position: 'relative',
        width: drawerWidth,
        // backgroundColor: '#1B5E20',
        // background: 'tomato',
    }
}

class LeftDrawer extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            open: true,
        }
    }

    handleDrawerOpen = () => {
        this.setState({ open: true });
    }

    handleDrawerClose = () => {
        this.setState({ open: false });
    }

    render() {
        const { classes } = this.props;

        return (
            <nav>
                <Drawer variant="permanent" anchor="left" open={this.state.open}
                    classes={{ paper: classes.drawerPaper, }}>

                    <Toolbar style={{'width': '100%',}}>
                        <IconButton>
                            <Avatar alt="গনপ্রজাতন্ত্রী বাংলাদেশ" src="/static/images/Flag-Bangladesh.ico" />
                        </IconButton>

                    </Toolbar>
                    <Divider />

                    <nav>
                        <LeftMenu></LeftMenu>
                    </nav>
                </Drawer>
            </nav>
        );
    }
}

export default withStyles(styles)(LeftDrawer);
