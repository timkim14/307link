import React, { Component } from 'react'
import Table from './Table'
import Form from './Form'
import axios from 'axios';

class App extends Component {
    constructor(props){
        super(props);
        this.state = {
            characters : []
        };
    }

    removeCharacter = id => {
        const self = this
        const { characters} = this.state
        
        return axios.delete(`http://localhost:5000/users/${id}`)
            .then(function(response){
                self.setState({
                    characters: characters.filter((character) =>{
                        return id !== character.id
                    })
                })
                console.log(response);
                return(response)
            })
            .catch(function(error){
                console.log(error);
                return false;
            });

        
    }

    makePostCall(character){
        return axios.post('http://localhost:5000/users', character)
            .then(function(response){
                console.log(response);
                return (response)
            })
            .catch(function(error){
                console.log(error);
                return false;
            });
    }

    handleSubmit = character =>{
        this.makePostCall(character).then( callResult =>{
            console.log(callResult)
            if(callResult.data.success) {
                this.setState({ characters: [...this.state.characters, callResult.data.newcharacter] });
                }
            }
        )
    }

    componentDidMount() {
        axios.get('http://localhost:5000/users')
         .then(res => {
           const characters = res.data.users_list;
           this.setState({ characters });
         })
         .catch(function (error) {
           console.log(error);
         });
    }

    render() {
        const { characters} = this.state
        return (
            <div className="container">
                <Table characterData={characters} removeCharacter ={this.removeCharacter}/>
                <Form handleSubmit = {this.handleSubmit}/>
            </div>
        );
    }
}

export default App