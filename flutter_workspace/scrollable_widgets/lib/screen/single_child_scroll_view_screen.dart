import 'package:flutter/material.dart';
import 'package:scrollable_widgets/const/colors.dart';
import 'package:scrollable_widgets/layout/main_layout.dart';

class SingleChildScrollViewScreen extends StatelessWidget {
  final List<int> numbers = List.generate(
    100,
    (index) => index,
  );

  SingleChildScrollViewScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    print(numbers);
    return MainLayout(
      title: 'SingleChildScrollView',
      body: renderPerformance(),
    );
  }

  // 1
  // rㄱㅣ본 렌더링법
  Widget renderSimple() {
    return SingleChildScrollView(
      child: Column(
        children: rainbowColors
            .map(
              (e) => renderContainer(color: e),
            )
            .toList(),
      ),
    );
  }

  // 2
  // 화면을 넘어가지 않아도 스크롤 되게 하기
  Widget renderAlwaysScroll() {
    return SingleChildScrollView(
      //physics: NeverScrollableScrollPhysics(), // 기본값 스크롤이 안됨
      physics: AlwaysScrollableScrollPhysics(), // 강제 스크롤 가능
      child: Column(
        children: [
          renderContainer(color: Colors.black),
        ],
      ),
    );
  }

  // 3
  // 화면 위젯이 잘리지 않게 하기
  Widget renderClip() {
    return SingleChildScrollView(
      clipBehavior: Clip.none,
      physics: AlwaysScrollableScrollPhysics(), // 강제 스크롤 가능
      child: Column(
        children: [
          renderContainer(color: Colors.black),
        ],
      ),
    );
  }

  // 4
  // 여러가지 phyics 정리
  Widget renderPhyics() {
    return SingleChildScrollView(
      //physics: NeverScrollableScrollPhysics(), // 스크롤 안됨
      //physics: AlwaysScrollableScrollPhysics(), // 스크롤 됨
      //physics: BouncingScrollPhysics(), // 안드로이드에서도 아이폰처럼 튕기듯이 스크롤 됨
      physics: ClampingScrollPhysics(), // 안드로이드 스타일
      child: Column(
        children: rainbowColors
            .map(
              (e) => renderContainer(color: e),
            )
            .toList(),
      ),
    );
  }

  // 5
  // SingleChildScrollView 퍼포먼스
  Widget renderPerformance(){
    return SingleChildScrollView(
      child: Column(
        children: numbers
            .map(
              (e) => renderContainer(
            color: rainbowColors[e % rainbowColors.length],
            index: e,
          ),
        ).toList(),
      ),
    );
  }

  Widget renderContainer({
    required Color color,
    int? index,
  }) {
    if(index != null){
      print(index);
    }
    return Container(
      height: 300,
      color: color,
    );
  }
}
