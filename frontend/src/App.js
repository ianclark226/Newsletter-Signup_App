import React, { useState } from 'react';
import './App.css';

const App = () => {
  const [agree, setAgree] = useState(false);
  const [formData, setFormData] = useState({
    first_name:'',
    email:'',
    
  });

  const { first_name, email } = formData;

  const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });
  const onChecked = e => setAgree(e.target.checked);

  const onSubmit = e => {
    e.preventDefault();
  }

  return (
    <div className="mt-5 d-flex flex-column justify-content-center align-items-center">
      <h1 className="display-4 mb-5">Sign up to our email list to recieve your FREE ebook!</h1>
      <form onSubmit={e => onSubmit(e)}>
        <div className="form-group mb-3">
          <label className="form-label">
            First Name:
          </label>
          <input className="form-control" type="text" name="first_name" onChange={e => onChange(e)}
          value={first_name} required />
        </div>
        <div className="form-group mb-3">
          <label className="form-label">
            Email:
          </label>
          <input className="form-control" type="email" name="email" onChange={e => onChange(e)}
          value={email} required />
        </div>
        <div className="form-group mb-3">
          <label style={{ marginRight: '6px' }} className="form-check-label">
            I agree to the privacy policy and terms of service.
          </label>
          <input className="form-check-input" type="checkbox" name="agree" onChange={e => onChecked(e)}
          checked={agree} required />
        </div>
        <button className="btn btn-success btn-lg mt-3">Give me my free ebook!</button>
      </form>
    </div>
  );
}

export default App;
