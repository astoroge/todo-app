import React from 'react'


class AuthForm extends React.Component {
    constructor(props) {
      super(props)
      this.state = {name: '', todos: []}
    }
  
    handleChange(event) 
    {    
        this.setState(
                {
                    [event.target.name]: event.target.value
                }
            );  
    }


    handleSubmit(event) {
      this.props.create_todo(this.state.name, this.state.todos)
      event.preventDefault()
    }
  
    render() {
      return (
        <form onSubmit={(event: FormEvent<HTMLFormElement>) => this.handleSubmit(event)}>
            
            <input type="text" name="name" 
            value={this.state.name} 
            onChange={(event)=>this.handleChange(event)}/>        
      
            <input type="submit" value="Save" />
        </form>
            
        
      );
    }
  }

  export default LoginForm