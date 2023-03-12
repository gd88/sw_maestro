// fit: BoxFit.cover >> 화면을 꽉 채움, 단 비율을 맞추기 위해 짤릴 수 있다

import 'dart:async';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {

  Timer? timer;
  PageController controller = PageController(
    // 초기화 할 페이지, 몇 번 째부터 시작할래
    initialPage: 0,
  );

  // initState()와 dispose()는 stful의 순환주기와 관련
  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    timer = Timer.periodic(Duration(seconds: 1), (timer) {
      // 초기페이지, double 타입이기에 int로 바꿔준다
      int currentPage = controller.page!.toInt();
      int nextPage = currentPage + 1;

      if (nextPage > 4) {
        nextPage = 0;
      }
      // 어떤 페이지로 애니메이션을 진행하라
      controller.animateToPage(
        nextPage,
        duration: Duration(seconds: 4),
        curve: Curves.linear,
      );
    });
  }

  // homescreen이 종료될 떄 실행된다
  // super.dispose()보다 위에 써줘야 종료 실행 전에 실행된다
  @override
  void dispose() {
    controller.dispose();
    if (timer != null) {
      timer!.cancel();
    }

    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    SystemChrome.setSystemUIOverlayStyle(SystemUiOverlayStyle.dark);

    return Scaffold(
      body: PageView(
        controller: controller,
        children: [1, 2, 3, 4, 5]
            .map(
              (e) => Image.asset(
                'asset/img/image_$e.jpeg',
                fit: BoxFit.cover,
              ),
            )
            .toList(),
      ),
    );
  }
}
