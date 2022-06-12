import 'dart:convert';

import 'package:http/http.dart' as http;

User userFromJson(String str) => User.fromJson(json.decode(str));

String userToJson(User data) => json.encode(data.toJson());

class User {
  int? id;
  String fullName;
  String username;
  String email;
  String password;
  bool active;
  String role;
  String cpf;

  User({
    this.id,
    required this.fullName,
    required this.username,
    required this.email,
    required this.password,
    this.active = true,
    required this.role,
    required this.cpf,
  });

  factory User.fromJson(Map<String, dynamic> json) {
    return User(
      id: json['id'] as int,
      fullName: json['fullName'] as String,
      username: json['username'] as String,
      email: json['email'] as String,
      password: json['password'] as String,
      active: json['active'] as bool,
      role: json['role'] as String,
      cpf: json['cpf'] as String,
    );
  }

  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'fullName': fullName,
      'username': username,
      'email': email,
      'password': password,
      'active': active,
      'role': role,
      'cpf': cpf,
    };
  }
}

