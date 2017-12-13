import React from 'react'

export default class Answer extends React.Component {
    // Initial State with default values
    state = {
        showList: false
    }

    // Method to handle the toggle of the list show / hide
    toggleList = (event) => {
        this.setState({
            showList: !this.state.showList
        })
        this.props.toggleList()
        document.getElementById("input_number").focus()
    }

    // Method to handle rendering the list of numbers on display and 
    // returning the DOM for it
    getListRender = (list) => {
        if(!list || !list.length) {
            return null
        }

        if(this.state.showList) {
            return (
                <div className="list-encloser">
                    <span className="iconify" onClick={this.toggleList}>⊖</span>
                    <hr className="separator"/>
                    <div>
                        <span className="dot"></span>
                        {
                            list.map((item, idx) => {
                                return (<span key={idx.toString()} className="arrow-down">
                                    <div className="answer subanswer" >{item}</div>
                                </span>)
                            })
                        }
                    </div>
                </div>
            )
        } else {
            return (
                <div className="list-encloser">
                    <span className="iconify" onClick={this.toggleList}>⊕</span>
                </div>
            )
        }
    }

    // Render life cycle method
	render = () => {

		return (
			<div className="answer-component">
				<h4 className="sub-heading">Fibonacci for {this.props.value}</h4>
                <h2 className="answer">{this.props.answer}</h2>
                {this.getListRender(this.props.intermediates)}
			</div>
		)
	}
}
