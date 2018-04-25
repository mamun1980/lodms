import React from 'react';
import { render } from 'react-dom';
import { BrowserRouter as Router, Route, Link, withRouter } from 'react-router-dom';

import Table from 'material-ui/Table';
// import { MuiThemeProvider, createMuiTheme } from 'material-ui/styles';
import Grid from 'material-ui/Grid';
// import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Drawer from 'material-ui/Drawer';
import Divider from 'material-ui/Divider';
import Paper from 'material-ui/Paper';
import Button from 'material-ui/Button';
import Typography from 'material-ui/Typography';
import Reboot from 'material-ui/Reboot';
// import List, { ListItem, ListItemIcon, ListItemText } from 'material-ui/List';

import Avatar from 'material-ui/Avatar';
// import DraftsIcon from 'material-ui-icons/Drafts';
// import SendIcon from 'material-ui-icons/Send';
import IconButton from 'material-ui/IconButton';
// import MenuIcon from 'material-ui-icons/Menu';
// import PhotoCamera from 'material-ui-icons/PhotoCamera';


import TopHeader from './components/common/topHeader';
import LeftDrawer from './components/common/leftDrawer';
import LeftMenu from './components/common/leftMenu';
// import LandDataTable from './components/landInfoTable';

import Test from './components/Test';
import Blog from './components/blog';
import Home from './Home';

const drawerWidth = 260;

const wrapper = {
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

const drawerPaper = {
    position: 'relative',
    width: drawerWidth,
    // backgroundColor: '#1B5E20',
    // background: 'tomato',
}

const content = {
    overflow: 'hidden',
    position: 'relative',
    flexGrow: 1,
    backgroundColor: '#FFF',
    marginTop: '80px',
    marginLeft: '15px',
    marginRight: '15px',
    marginBottom: '15px',
    padding: '15px',
}


class App extends React.Component {

    constructor(props) {
        super(props)
        this.state = {
            open: true,
        }
    }

    render() {

        return (

            <div style={wrapper}>
                <Reboot />
                <Router>
                    <div style={appFrame}>

                        <TopHeader></TopHeader>
                        <LeftDrawer></LeftDrawer>

                        <Grid container style={content}>
                            <Grid item xs={12}>

                                <Typography>{'You think water moves fast? You should see ice.'}</Typography>

                            </Grid>
                            <Grid item xs={9}>
                                <Route exact path="/" component={Home}/>
                                <Route path="/blog" component={Blog}/>
                                <Route path="/test" component={Test}/>
                            </Grid>
                            <Grid item xs={3}>
                                <p>hello</p>
                            </Grid>

                        </Grid>
                    </div>
                </Router>

            </div>

        );
    }
}

render(<App />, document.querySelector('#lodms_root'));
