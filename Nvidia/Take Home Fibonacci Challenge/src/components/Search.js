import React from 'react'

export default class Search extends React.Component {

	// Initial State with default values
	state = {
        value: 0
	}
	
	// When component mounts DOM, initialize focus to the one and 
	// only field on page
	componentDidMount = () => {
		document.getElementById("input_number").focus()
	}

	// Method to handle the change in input value and trigger the 
	// fibonacci calculation on number field value change
	handleChange = (event) => {
		if(event.target.value === "") {
			event.target.value = 0
		}
		event.target.value = parseInt(event.target.value, 10)
		this.props.onSearch(event.target.value)
	}

	// Render lifecycle method
	render = () => {

		return (
			<div className="search-component">
				<input type="number" id="input_number" placeholder="0"
				onChange={this.handleChange.bind(this)} className="search-bar"/>
			</div>
		)

	}

}
