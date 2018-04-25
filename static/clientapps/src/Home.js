import React from 'react';
import PropTypes from 'prop-types';

export class Home extends React.Component {
    constructor(props) {
        super();
        this.state = {
            homeLink: "HomeInit"
        }
    }

    onChangeLink() {
        this.props.changeLink(this.state.homeLink);
    }

    render() {
        return (
            <div id="home">
                <h2>{this.props.children}</h2>
                <h3>My name is {this.props.name}</h3>
                <button onClick={this.props.greet}>Greet</button>
                <hr/>
                <input type="text" onChange={this.onChangeLink.bind(this)} />
            </div>
        );
    }
}

// Home.propTypes = {
//     name: React.PropTypes.string,
//     children: React.PropTypes.element.isRequired
// };
