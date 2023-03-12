import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';


class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  DateTime selectedDate = DateTime(
    DateTime.now().year,
    DateTime.now().month,
    DateTime.now().day,
  );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.pink[100], //[500]이 기본값
        body: SafeArea(// 폰 범위를 넘으므로 넣어준다
          bottom: false,
          child: Container(  // column만 하면 왼쪽 우측에 생기므로 container를 넣고 width를 넓힌다
            width: MediaQuery.of(context).size.width ,
            child: Column(
              children: [
                _TopPart(
                  selectedDate: selectedDate,
                  onpressed: onHeartPressed,
                ),
                _BottomPart(),
              ],
            ),
          ),
        )
    );
  }





 void onHeartPressed(){
    final DateTime now = DateTime.now();

      // dialog(화면을 덮는 또 하나의 화면을 만듬, 그 화면 안에 들어갈 위젯을 builder에 넣어준다)
      // builder는 build함수라고 생각
      showCupertinoDialog(
        context: context,
        // 밖에 누르면 닫힌다
        barrierDismissible: true,
        builder: (BuildContext context){
          return Align(// 정렬, 그냥 container만 하면 어디에 정렬하지 모르기에 다 덮어버린다
            alignment: Alignment.bottomCenter,
            child: Container(
              color: Colors.white,
              height: 300.0,
              child: CupertinoDatePicker(
                mode: CupertinoDatePickerMode.date,
                initialDateTime: selectedDate,
                maximumDate: DateTime(
                  now.year,
                  now.month,
                  now.day,
                ),
                onDateTimeChanged: (DateTime date){
                  // 변수를 변경할 때, build를 다시 실행시킬 때 사용
                  setState(() {
                    selectedDate = date;
                  });
                },
              ),
            ),
          );
        },
      );
    }
}






class _TopPart extends StatelessWidget {
  // selectedDate: 처음엔 지금으로 하고 변경할 때마다 부여

  final DateTime selectedDate;
  final VoidCallback onpressed;

  _TopPart({
    required this.selectedDate,
    required this.onpressed,
    Key? key}
      ): super(key:key);


  @override
  Widget build(BuildContext context) {
    // 밑에 context는 build 안에 context이다
    // theme.of(context)는 가장 가까운 위젯의 theme인스턴스를 가져올 수 있다
    final theme = Theme.of(context);
    final textTheme = theme.textTheme;
    final now = DateTime.now();


    return  Expanded(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Text(
            'U&I',
            style: textTheme.headline1,
          ),
          Column(
            children: [
              Text('우리 처음 만난 날',
                  style: textTheme.bodyText1),
              Text('${selectedDate.year}.${selectedDate.month}.${selectedDate.day}',
                    style: textTheme.bodyText2,
              ),
            ],
          ),
          IconButton(
            iconSize: 60.0,
            onPressed: onpressed,
            icon: Icon(
              Icons.favorite,
              color: Colors.red,
            ),),
          Text('D+${
          DateTime(
            now.year,
            now.month,
            now.day,
          ).difference(selectedDate).inDays+1
          }',
            style: textTheme.headline2,
          )
        ],
      ),
    );
  }
}


class _BottomPart extends StatelessWidget {
  const _BottomPart({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Image.asset(
          'asset/img/middle_image.png'),
    );
  }
}
