import React from 'react';
import { render } from 'react-dom';


import { MuiThemeProvider, createMuiTheme } from 'material-ui/styles';
import Grid from 'material-ui/Grid';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Drawer from 'material-ui/Drawer';
import Divider from 'material-ui/Divider';
import Paper from 'material-ui/Paper';
import Button from 'material-ui/Button';
import Typography from 'material-ui/Typography';
import Reboot from 'material-ui/Reboot';
import List, { ListItem, ListItemIcon, ListItemText } from 'material-ui/List';

import DraftsIcon from 'material-ui-icons/Drafts';
import SendIcon from 'material-ui-icons/Send';
import IconButton from 'material-ui/IconButton';
import MenuIcon from 'material-ui-icons/Menu';
import PhotoCamera from 'material-ui-icons/PhotoCamera';



const drawerWidth = 240;
const wrapper = {
    // zIndex: 1,
    // overflow: 'hidden',
    // position: 'relative',
    // display: 'flex',
    // flexWrap: 'wrap',
    background: 'tomato',
    flexGrow: 1
}

const appFrame = {
    height: '100vh',
    zIndex: 1,
    overflow: 'hidden',
    position: 'relative',
    display: 'flex',
    width: '100%',
}

const appBar = {
    width: `calc(100% - ${drawerWidth}px)`,
    marginLeft: drawerWidth
}

const menuButton = {
    marginLeft: 12,
    marginRight: 20,
}

const hideleft = {
    display: 'none'
}

const drawerPaper = {
    position: 'relative',
    width: drawerWidth
}



const content = {
    overflow: 'hidden',
    position: 'relative',
    flexGrow: 1,
    backgroundColor: '#cFc',
}


class App extends React.Component {

    constructor() {
        super()
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

        return (
            <div style={wrapper}>
                <Reboot />
                
                <div style={appFrame}>
                    
                    <AppBar style={appBar}>
                        <Toolbar>
                            <IconButton style={menuButton} color="inherit" aria-label="Menu">
                                <MenuIcon />
                            </IconButton>
                            <Typography variant="title" color="inherit" noWrap>
                                Persistent drawer
                            </Typography>
                        </Toolbar>
                    </AppBar>

                    <Drawer variant="permanent" anchor="left" open={true} style={drawerPaper}>
                        
                            <Toolbar style={{'width': '240px'}}>
                                <IconButton>
                                    <PhotoCamera />
                                </IconButton>    
                            </Toolbar>
                            <Divider />

                            <List>
                                <ListItem button>
                                    <ListItemIcon>
                                      <SendIcon />
                                    </ListItemIcon>
                                    <ListItemText inset primary="Sent mail" />
                                </ListItem>
                                <ListItem button>
                                    <ListItemIcon>
                                      <DraftsIcon />
                                    </ListItemIcon>
                                    <ListItemText inset primary="Drafts" />
                                </ListItem>
                            </List>
                        
                    </Drawer>

                </div>
            </div>
        );
    }
}

render(<App />, document.querySelector('#casems_root'));
