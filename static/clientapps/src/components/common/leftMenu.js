import React from 'react';
import { Link, withRouter } from 'react-router-dom';

import PropTypes from 'prop-types';

import Toolbar from 'material-ui/Toolbar';
import Typography from 'material-ui/Typography';
import List, { ListItem, ListItemIcon, ListItemText } from 'material-ui/List';
import Collapse from 'material-ui/transitions/Collapse';
import { withStyles } from 'material-ui/styles';

import MenuIcon from 'material-ui-icons/Menu';
import IconButton from 'material-ui/IconButton';
import PhotoCamera from 'material-ui-icons/PhotoCamera';
import DraftsIcon from 'material-ui-icons/Drafts';
import SendIcon from 'material-ui-icons/Send';
import StarBorder from 'material-ui-icons/StarBorder';
import ExpandLess from 'material-ui-icons/ExpandLess';
import ExpandMore from 'material-ui-icons/ExpandMore';


const nested = {
    paddingLeft: '20px !important',
}

const styles = {
    inset: {
        paddingLeft: '5px !important'
    },
    root: {
        paddingLeft: '25px !important',
        // background: '#eee',
        // boxShadow: 'inset 0 0 10px #000000;'
    },
    ListItemText: {
        paddingLeft: '10px',

    }
}


class LeftMenu extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            casemenu: false,
            landmenu: false
        }
    }

    handleCaseMenu = () => {
        // console.log(this.props);
        this.setState({ casemenu: !this.state.casemenu });
        this.props.history.push('/test');

    };

    handleLandMenu = () => {
        this.setState({ landmenu: !this.state.landmenu });
        this.props.history.push('/blog');
    };

    render() {

        const { classes, history } = this.props

        return (

            <List>
                <ListItem button onClick={this.handleLandMenu.bind(this)}>

                    <ListItemText inset primary="মামলা মোকদ্দমার তথ্য "
                    classes={{ root: classes.ListItemText, inset: classes.inset }} />
                    {this.state.landmenu ? <ExpandLess /> : <ExpandMore />}
                </ListItem>
                <Collapse in={this.state.landmenu} timeout="auto" unmountOnExit>
                    <List component="div" disablePadding >
                        <ListItem button >

                            <ListItemText inset primary="বন্দোবস্ত জমি" classes={{ root: classes.root, }} />
                        </ListItem>
                        <ListItem button >

                            <ListItemText inset primary="অর্পিত সম্পত্তি " classes={{ root: classes.root, }} />
                        </ListItem>
                    </List>
                </Collapse>

                <ListItem button onClick={this.handleCaseMenu.bind(this)}>

                    <ListItemText inset primary="জমির তথ্য " classes={{ root: classes.ListItemText, inset: classes.inset }} />
                    {this.state.casemenu ? <ExpandLess /> : <ExpandMore />}
                </ListItem>
                <Collapse in={this.state.casemenu} timeout="auto" unmountOnExit>
                    <List component="div" disablePadding>
                        <ListItem button >

                            <ListItemText inset primary="খাস জমির তথ্য " classes={{ root: classes.root, }} />
                        </ListItem>
                        <ListItem button >

                            <ListItemText inset primary="বন্দোবস্ত জমি" classes={{ root: classes.root, }} />
                        </ListItem>
                        <ListItem button >

                            <ListItemText inset primary="অর্পিত সম্পত্তি " classes={{ root: classes.root, }} />
                        </ListItem>
                        <ListItem button >

                            <ListItemText inset primary="রেকর্ডীয় জমি তথ্য" classes={{ root: classes.root, }} />
                        </ListItem>
                        
                        <ListItem button component={Link} to='/test'>

                            <ListItemText inset primary="Test" classes={{ root: classes.root, }} />
                        </ListItem>
                        <ListItem button component='a' href='/hello'>

                            <ListItemText inset primary="Hello" classes={{ root: classes.root, }} />
                        </ListItem>
                    </List>
                </Collapse>
            </List>


        );
    }
}

export default withStyles(styles)(withRouter(LeftMenu))
