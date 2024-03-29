import 'package:flutter/material.dart';
import 'package:navigation/screen/home_screen.dart';
import 'package:navigation/screen/route_one_screen.dart';
import 'package:navigation/screen/route_three_screen.dart';
import 'package:navigation/screen/route_two_screen.dart';

void main() {
  runApp(
    MaterialApp(
      //home: HomeScreen(),
      initialRoute: '/',
      routes: {
        '/' : (context) => HomeScreen(),
        '/one' : (context) => RouteOneScreen(),
        '/tow' : (context) => RouteTwoScreen(),
        '/three' : (context) => RouteThreeScreen(),
      }
    ),
  );
}
