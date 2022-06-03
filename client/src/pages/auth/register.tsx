import { NextPage } from "next";
import Link from "next/link";

const Register: NextPage = () => {
    return (
        <>
            <h1>Register new User</h1>
            <p><Link href="/auth/login"><a>Click to Login</a></Link></p>

            <form action="" method="post">
                <label htmlFor="full_name">Full Name</label>
                <input type="text" name="full_name" id="full_name" />
                <label htmlFor="username">Username</label>
                <input type="text" name="username" id="username" />
                <label htmlFor="email">Email</label>
                <input type="email" name="email" id="email" />
                <label htmlFor="password">Password</label>
                <input type="password" name="password" id="password" />
                <label htmlFor="role">Role</label>
                <input type="text" name="role" id="role" />
                <label htmlFor="cpf">CPF</label>
                <input type="text" name="cpf" id="cpf" />
                <button type="submit">Register</button>
            </form>
        </>
    );
};

export default Register;