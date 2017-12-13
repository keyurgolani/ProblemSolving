import React from 'react'

import Search from './components/Search'
import Answer from './components/Answer'

export default class App extends React.Component {

    // Initial State is Empty. Will initialize once the component mounts
    state = {}

    // State Initialization on component mount
    componentDidMount = () => {
        const fibonacci = 0
        const value = 0

        // Initial values for Fibonacci
        var caches = [0, 1]

        // Storing precalculated values to the localStore in order to 
        // cache them at the app start and calculate fibonacci faster
        if(localStorage.caches) {
			caches = JSON.parse(localStorage.caches)
		}

        this.setState({
            fibonacci: fibonacci,
			caches: caches,
            value: value,
            intermediates: [],
            toggleList: false
		})
    }

    findFibonacci = (value, caches) => {
        // If value is already calculated and cached, use that.
        // No updates to the cache
        if(value < caches.length - 1) {
            return {
                answer: caches[value],
                caches: caches
            }
        // If the value entered is more than 1476, the fibonacci
        // number for that is not handlable for JavaScript hence
        // give back Infinity without using resources in calculation
        } else if(value > 1476) {
            for(let i = caches.length; i <= 1477; i++) {
                caches.push(
                    caches[i - 1] + caches[i - 2]
                )
            }
            return {
                answer: Infinity,
                caches: caches
            }
        // Otherwise, calculate the fibonacci numbers till given value
        // index & keep updating the cache. Return final value and cache
        } else {
            for(let i = caches.length; i <= value; i++) {
                caches.push(
                    caches[i - 1] + caches[i - 2]
                )
            }
            return {
                answer: caches[value],
                caches: caches
            }
        }
    }

    // Update the stored cache whenever new cache is updated.
    updateLocalCache = (caches) => {
        localStorage.caches = JSON.stringify(caches)
    }

    // Calculate the fibonacci for given number and manage the cache
    // during the calculation.
    updateFibonacci = (value) => {

		const self = this

        const caches = this.state.caches

        const response = this.findFibonacci(value, caches)
        if(caches) {
            this.updateLocalCache(response.caches)
        }

        self.setState({
            fibonacci: response.answer,
			caches: response.caches,
            value: value,
            intermediates: response.caches.slice(0, parseInt(value, 10)+1),
            toggleList: this.state.toggleList
		})

    }
    
    // Setting and resetting toggleList to set the overlay height accordingly.
    toggleList = () => {
        this.setState({
            ...this.state,
            toggleList: !this.state.toggleList
        })
    }

    // Render lifecycle method
	render = () => {

		return (
            <div>
                <h1 className="title">Enter Number to Find Fibonacci</h1>
                <Search onSearch={this.updateFibonacci.bind(this)} />
                <div id="layover" className={this.state.toggleList?"layover layover-expandable":"layover"}>
                    <Answer answer={this.state.fibonacci} intermediates={this.state.intermediates} value={this.state.value} toggleList={this.toggleList.bind(this)}/>
                </div>
            </div>

		)
	}
}
