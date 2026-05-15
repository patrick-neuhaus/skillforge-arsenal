import 'package:flutter/material.dart';

class Aa extends StatefulWidget {

  const Aa({ super.key });

  @override
  State<Aa> createState() => _AaState();
}

class _AaState extends State<Aa> {

   @override
   Widget build(BuildContext context) {
       return Scaffold(
           appBar: AppBar(title: const Text(''),),
           body: Container(),
       );
  }
}