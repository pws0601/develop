import 'package:flutter/material.dart';
import 'package:navigation/layout/main_layout.dart';
import 'package:navigation/screen/route_one_screen.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return WillPopScope(
      onWillPop: () async {
        // 안드로이드에서 뒤로가기로 앱종료 true/false
        // true - pop 가능
        // false = pop 불가능
        final canPop = Navigator.of(context).canPop();
        return canPop;
      },
      child: MainLayout(title: 'Home Screen', children: [
        ElevatedButton(
          onPressed: () {
            print(Navigator.of(context).canPop());
          },
          child: Text('Can Pop'),
        ),
        ElevatedButton(
          onPressed: () {
            Navigator.of(context).maybePop();
          },
          child: Text('maybePop'),
        ),
        ElevatedButton(
          onPressed: () {
            Navigator.of(context).pop();
          },
          child: Text('Pop'),
        ),
        ElevatedButton(
          onPressed: () async {
            final result = await Navigator.of(context).push(
              MaterialPageRoute(
                builder: (BuildContext context) => RouteOneScreen(
                  number: 123,
                ),
              ),
            );

            print(result);
          },
          child: Text('Push'),
        ),
      ]),
    );
  }
}
