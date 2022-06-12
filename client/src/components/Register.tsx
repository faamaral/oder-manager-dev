import { type } from "os";
import React from "react";

import { IRegister } from "../types";

type Props = {
    saveUser: (e: React.FormEvent, formData: IRegister) => void;
}

const Register: React.FC<Props> = ({ saveUser }) => {
    const [formData, setFormData] = React.useState<IRegister>({
        full_name: "",
        username: "",
        email: "",
        password: "",
        role: "",
        cpf: "",
    });

    const handleForm = (e: React.ChangeEvent<HTMLInputElement>) : void => {
        setFormData({
            ...formData,
            [e.currentTarget.id]: e.currentTarget.value
        });
    }
    return (
        <form onSubmit={(e) => saveUser(e, formData)}>
            <div>
                <div className="Form--field">
                    <label htmlFor="full_name"> Full Name</label>
                    <input type="text" name="full_name" id="full_name" onChange={handleForm}/>
                </div>
                <div className="Form--field">
                    <label htmlFor="username"> Username</label>
                    <input type="text" name="username" id="username" onChange={handleForm}/>
                </div>
                <div className="Form--field">
                    <label htmlFor="email"> Email</label>
                    <input type="email" name="email" id="email" onChange={handleForm}/>
                </div>
                <div className="Form--field">
                    <label htmlFor="password"> Password</label>
                    <input type="password" name="password" id="password" onChange={handleForm}/>
                </div>
                <div className="Form--field">
                    <label htmlFor="password_confirmation"> Password Confirmation</label>
                    <input type="password" name="password_confirmation" id="password_confirmation"/>
                </div>
                <div className="Form--field">
                    <label htmlFor="role"> Role</label>
                    <input type="text" name="role" id="role" onChange={handleForm}/>
                </div>
                <div className="Form--field">
                    <label htmlFor="cpf"> CPF</label>
                    <input type="text" name="cpf" id="cpf" onChange={handleForm}/>
                </div>
                
            </div>
            <button className="Form__button" type="submit" disabled={formData === undefined ? true : false}>Register</button>
        </form>
    );
}

export default Register;