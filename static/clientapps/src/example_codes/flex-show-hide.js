import React from 'react';
import { render } from 'react-dom';

import { MuiThemeProvider, createMuiTheme } from 'material-ui/styles';

import Grid from 'material-ui/Grid';
import AppBar from 'material-ui/AppBar';
import Toolbar from 'material-ui/Toolbar';
import Drawer from 'material-ui/Drawer';
import Paper from 'material-ui/Paper';
import Button from 'material-ui/Button';
import Reboot from 'material-ui/Reboot';

const leftside = {
    flexGrow: 0,
    flexShrink: 1,
    backgroundColor: '#fcc',
    height: '250px',
    width: '240px'
}

const hideleft = {
    display: 'none'
}

const rightside = {
    flexGrow: 1,
    flexShrink: 0,
    backgroundColor: '#ccc',
    height: '250px'
}

const wrapper = {
    zIndex: 1,
    overflow: 'hidden',
    position: 'relative',
    display: 'flex',
    flexWrap: 'wrap',
    background: 'tomato'
}

const content = {
    overflow: 'hidden',
    position: 'relative',
    flexGrow: 1,
    backgroundColor: '#cFc',
    height: '100px',
    width: '100%',
    border: '2px',
    marginTop: '20px'
}


class App extends React.Component {

    constructor() {
        super()
        this.state = {
            showleft: true,
        }
    }

    toggleLeftSide(e) {
        
        this.setState({
            showleft: !this.state.showleft
        })
    }

    render() {

        return (
            <div style={wrapper}>
                <Reboot />
                <div style={this.state.showleft ? leftside : {'display': 'none'} }>
                    leftside
                </div>
                <div style={rightside}>
                    Right side
                </div>
                <div style={content}>
                    <Button onClick={this.toggleLeftSide.bind(this)}>HidenShow</Button>
                </div>
            </div>
        );
    }
}

render(<App />, document.querySelector('#casems_root'));
