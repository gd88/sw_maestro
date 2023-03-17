import 'package:flutter/material.dart';
import 'package:random_number_generator/constant/color.dart';

// homescreen에서 settingscreen을 push하고 pop하면 아예 사라지는 거임
// 그리고 다시 클릭하면 다시 생성되는 거고
class SettingsScreen extends StatefulWidget {
  final int maxNumber;

  const SettingsScreen({required this.maxNumber, Key? key}) : super(key: key);

  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> {
  // 여기 있는 변수 선언들은 state가 생성이 되기 전에 stful에 붙기 전에 생성되므로
  // double maxNumber = widget.maxNumber; 안된다
  double maxNumber = 1000;

  @override
  void initState() {
    super.initState();

    maxNumber = widget.maxNumber.toDouble();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: PRIMARY_COLOR,
      body: SafeArea(
        child: Padding(
          padding: EdgeInsets.symmetric(horizontal: 16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              _Body(maxNumber: maxNumber),
              _Footer(
                maxNumber: maxNumber,
                onSliderChanged: onSliderChanged,
                onButtonPressed: onButtonPressed,
              ),
            ],
          ),
        ),
      ),
    );
  }

  onSliderChanged(double val) {
    setState(() {
      maxNumber = val;
    });
  }

  onButtonPressed() {
    // pop 하면서 homescreen으로 maxnumber 돌려주기
    Navigator.of(context).pop(maxNumber.toInt());
  }
}

class _Body extends StatelessWidget {
  final double maxNumber;
  const _Body({required this.maxNumber, Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Row(
        children: maxNumber
            .toInt()
            .toString()
            .split('')
            .map(
              (e) => Image.asset(
                'asset/img/$e.png',
                width: 50,
                height: 70,
              ),
            )
            .toList(),
      ),
    );
  }
}

class _Footer extends StatelessWidget {
  final double maxNumber;
  final ValueChanged<double>? onSliderChanged;
  final VoidCallback onButtonPressed;

  const _Footer({
    required this.maxNumber,
    required this.onSliderChanged,
    required this.onButtonPressed,
    Key? key,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.stretch,
      children: [
        // val = slider를 움직였을 때 움진인 만큼의 값을 의미하는 값
        // onchanged가 불릴 때 maxnumber에 변경된 값(val=현재 슬라이더의 위치)을 넣어주고
        // build가 다시 되어 변경된 값이 다시 slider value:에 들어가 현재 슬라이더의 위치를 표시해준다
        Slider(
          value: maxNumber,
          min: 1000,
          max: 1000000,
          onChanged: onSliderChanged,
        ),
        ElevatedButton(
          onPressed: onButtonPressed,
          style: ElevatedButton.styleFrom(
            primary: RED_COLOR,
          ),
          child: Text('저장'),
        )
      ],
    );
  }
}
