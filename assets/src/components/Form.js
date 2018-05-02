import React from 'react';

const Form = props => (
  <form onSubmit={props.getLogin}>
    <input type="text" name="username" placeholder="Usuario..." />
    <input type="password" name="password" placeholder="Senha..." />
    <button>Entrar</button>
  </form>
);

export default Form;

