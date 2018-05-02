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
    const form = new FormData();
    form.append('name', user); 
    form.append('password', password); 

    // const apiCall = await fetch(`https://flasklogin.herokuapp.com/autenticar?name=${user}&password=${password}`);
    const apiCall = await fetch('https://flasklogin.herokuapp.com/autenticar', {
      method: 'POST',
      mode: 'no-cors',
      headers: {
        'Content-Type': 'application/json',
      },
      body: form
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
