import React from 'react';

import Form from './components/Form';

class App extends React.Component {
  state = {
    userName: undefined,
    error: ''
  }

  getLogin = async (e) => {
    e.preventDefault();

    const user = e.target.elements.username.value;
    const password = e.target.elements.password.value;

    const apiCall = await fetch('http://192.168.1.6:5000/login', {
      method: 'POST',
      mode: 'no-cors',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: JSON.stringify({
        "name": user,
        "password": password,
      })
    });
    const data = await apiCall.json();

    if(user && password) {
      if(data.status === 0) {
        this.setState({
          userName: data.name,
          error: ''
        });
        console.log(data);
      } else {
        this.setState({
          userName: undefined,
          error: data.message
        });
        console.log(data);
      }
    } else {
      this.setState({
        userName: undefined,
        error: 'Informe o usuario e senha'
      });
    }
  }

  render() {
    return (
      <div>
        <Form getLogin={this.getLogin} />
      </div>
    );
  }
}

export default App;
