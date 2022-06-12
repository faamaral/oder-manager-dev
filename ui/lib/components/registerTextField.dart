import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';

class RegisterTextField extends StatelessWidget {
  final String label;
  final TextEditingController controller;
  final TextInputType? keyboardType;
  final bool obscureText;
  final String hintText;
  final IconData icon;
  final Function(String? value) validator;
  const RegisterTextField({
    Key? key,
    required this.label,
    required this.controller,
    required this.hintText,
    this.keyboardType,
    this.obscureText = false,
    required this.icon,
    required this.validator,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      controller: controller,
      keyboardType: keyboardType != null ? keyboardType : TextInputType.text,
      obscureText: obscureText,
      // validator: validator,
      decoration: InputDecoration(
          labelText: label, hintText: hintText, border: OutlineInputBorder(), prefixIcon: Icon(icon)),
    );
  }
}
