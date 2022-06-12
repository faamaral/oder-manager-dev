import 'dart:convert';

import 'package:email_validator/email_validator.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:mask_text_input_formatter/mask_text_input_formatter.dart';
import 'package:ui/model/user.dart';
import 'package:http/http.dart' as http;

class RegisterForm extends StatefulWidget {
  const RegisterForm({Key? key}) : super(key: key);

  @override
  State<RegisterForm> createState() => _RegisterFormState();
}

class _RegisterFormState extends State<RegisterForm> {
 final _formKey = GlobalKey<FormState>();

  final _fullNameController = TextEditingController();
  final _usernameController = TextEditingController();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();
  final _roleController = TextEditingController();
  final _cpfController = TextEditingController();

  final _cpfFormatter = MaskTextInputFormatter(
      mask: '###.###.###-##', filter: {'#': RegExp(r'[0-9]')});
  bool _obscureText = true;
  String _selectedRole = 'User';
  String _emailError = '';
  final roles = [
    'Administrator',
    'User',
  ];

  void _showPassword() {
    setState(() {
      _obscureText = !_obscureText;
    });
  }

  void validateEmail(String value) {
    if (value.isEmpty) {
      setState(() {
        _emailError = 'Email is required';
      });
    } else if (!EmailValidator.validate(value, true)) {
      setState(() {
        this._emailError = 'Invalid email address';
      });
    } else {
      setState(() {
        this._emailError = '';
      });
    }
  }

  void createUser(String fullName, String username,
      String email, String password, String role, String cpf) async {
    final response = await http.post(Uri.http('localhost:5000', '/auth/register'),
        headers: <String, String>{
          'Content-Type': 'application/json; charset=UTF-8',
        },
        body: jsonEncode(<String, String>{
          "full_name": fullName,
          "username": username,
          "email": email,
          "password": password,
          "role": role,
          "cpf": cpf,
        }));
    final data = response.body;
    print(data);

    if (response.statusCode == 201) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to create user');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Card(
        color: Colors.cyan[100],
        elevation: 5,
        margin: const EdgeInsets.all(20),
        child: Form(
          key: _formKey,
          child: Padding(
            padding: const EdgeInsets.all(8.0),
            child: Column(
              children: [
                TextFormField(
                  autovalidateMode: AutovalidateMode.onUserInteraction,
                  obscureText: false,
                  controller: _fullNameController,
                  validator: (value) =>
                      value!.isEmpty ? 'Full name is required' : null,
                  decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Full Name',
                      prefixIcon: Icon(Icons.person_pin)),
                ),
                SizedBox(height: 10),
                TextFormField(
                  autovalidateMode: AutovalidateMode.onUserInteraction,
                  controller: _usernameController,
                  validator: (value) =>
                      value!.isEmpty ? 'Username is required' : null,
                  decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Username',
                      prefixIcon: Icon(Icons.person_rounded)),
                ),
                SizedBox(height: 10),
                TextFormField(
                  autovalidateMode: AutovalidateMode.onUserInteraction,
                  controller: _emailController,
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Email is required';
                    } else if (!EmailValidator.validate(value, true)) {
                      return 'Invalid email address';
                    } else {
                      return null;
                    }
                  },
                  keyboardType: TextInputType.emailAddress,
                  // onChanged: (value) => this.validateEmail(value),
                  decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Email',
                      prefixIcon: Icon(Icons.mail_rounded)),
                ),
                SizedBox(height: 10),
                TextFormField(
                  autovalidateMode: AutovalidateMode.onUserInteraction,
                  obscureText: _obscureText,
                  obscuringCharacter: '*',
                  controller: _passwordController,
                  validator: (value) =>
                      value!.isEmpty ? 'Password is required' : null,
                  decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      labelText: 'Password',
                      prefixIcon: Icon(Icons.lock_rounded),
                      suffixIcon: Padding(
                        padding: EdgeInsets.fromLTRB(0, 0, 4, 0),
                        child: GestureDetector(
                          onTap: _showPassword,
                          child: Icon(
                            _obscureText
                                ? Icons.visibility_rounded
                                : Icons.visibility_off_rounded,
                          ),
                        ),
                      )),
                ),
                SizedBox(height: 10),
                TextFormField(
                  autovalidateMode: AutovalidateMode.onUserInteraction,
                  obscureText: _obscureText,
                  obscuringCharacter: '*',
                  controller: _confirmPasswordController,
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Confirm password is required';
                    } else if (value != _passwordController.text) {
                      return 'Passwords do not match';
                    } else {
                      return null;
                    }
                  },
                  decoration: InputDecoration(
                      border: OutlineInputBorder(),
                      errorBorder: OutlineInputBorder(
                          borderSide: BorderSide(color: Colors.red)),
                      labelText: 'Confirm Password',
                      prefixIcon: Icon(Icons.lock_rounded),
                      suffixIcon: Padding(
                        padding: EdgeInsets.fromLTRB(0, 0, 4, 0),
                        child: GestureDetector(
                          onTap: _showPassword,
                          child: Icon(
                            _obscureText
                                ? Icons.visibility_rounded
                                : Icons.visibility_off_rounded,
                          ),
                        ),
                      )),
                ),
                SizedBox(height: 10),
                DropdownButtonFormField(
                  autovalidateMode: AutovalidateMode.onUserInteraction,
                    hint: Text('Select a Role'),
                    icon: Icon(Icons.arrow_downward_rounded),
                    decoration: InputDecoration(
                        border: OutlineInputBorder(),
                        labelText: 'Select a Role',
                        prefixIcon: Icon(Icons.work_rounded)),
                    elevation: 16,
                    style: TextStyle(
                      color: Colors.blueGrey[700],
                    ),
                    value: _selectedRole,
                    items: roles
                        .map<DropdownMenuItem<String>>(
                            (String value) => DropdownMenuItem<String>(
                                  child: Text(value),
                                  value: value,
                                ))
                        .toList(),
                    onChanged: (String? newValue) {
                      setState(() {
                        _selectedRole = newValue!;
                      });
                    }),
                SizedBox(height: 10),
                TextFormField(
                  autovalidateMode: AutovalidateMode.onUserInteraction,
                  inputFormatters: [_cpfFormatter],
                  validator: (value) => value!.isEmpty ? 'CPF is required' : null,
                  controller: _cpfController,
                  // maxLength: 11,
                  decoration: InputDecoration(
                      prefixIconColor: Colors.blueGrey[700],
                      border: OutlineInputBorder(),
                      labelText: 'CPF',
                      prefixIcon: Icon(Icons.text_snippet_rounded)),
                ),
                SizedBox(height: 10),
                ElevatedButton(
                  onPressed: () {
                    setState(() {
                      createUser(
                          _fullNameController.text,
                          _usernameController.text,
                          _emailController.text,
                          _passwordController.text,
                          _selectedRole,
                          _cpfController.text);
                    });
                  },
                  child: Text('Register'),
                  style: ElevatedButton.styleFrom(primary: Colors.blueGrey[700]),
                )
              ],
            ),
          ),
        ));
  }
}
