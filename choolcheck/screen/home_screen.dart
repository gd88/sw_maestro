import 'package:flutter/material.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  bool choolCheckDone = false;
  GoogleMapController? mapController;
  // latitude - 위도, longtitude - 경도
  // 지도의 첫 위치
  static final LatLng companyLatLng = LatLng(
    37.55769913670688,
    127.04587054138098,
  );
  // zoom level
  static final CameraPosition initialPosition = CameraPosition(
    target: companyLatLng,
    zoom: 15,
  );
  // 원
  // circleid가 같은 동그라민지 다른 동그라민지 구분지을 수 있게 한다

  static final double okDistance = 100;
  // device의 위치가 바뀌는 상황마다 다른 색의 원을 넣어준다
  // 원 안에 있는지 없는지를 구분할 수 있게 해준다
  //
  static final Circle withinDistanceCircle = Circle(
    circleId: CircleId('withinDistanceCircle'),
    center: companyLatLng,
    fillColor: Colors.blue.withOpacity(0.5),
    radius: okDistance,
    strokeColor: Colors.blue,
    strokeWidth: 1,
  );
  //
  static final Circle notWithinDistanceCircle = Circle(
    circleId: CircleId('notWithinDistanceCircle'),
    center: companyLatLng,
    fillColor: Colors.red.withOpacity(0.5),
    radius: okDistance,
    strokeColor: Colors.red,
    strokeWidth: 1,
  );
  //
  static final Circle checkDoneCircle = Circle(
    circleId: CircleId('checkDoneCircle'),
    center: companyLatLng,
    fillColor: Colors.green.withOpacity(0.5),
    radius: okDistance,
    strokeColor: Colors.green,
    strokeWidth: 1,
  );
  static final Marker marker = Marker(
    markerId: MarkerId('marker'),
    position: companyLatLng,
  );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: renderAppBar(),
      // initialCameraPosition: 처음 구긁 지도를 켰을 때 어느 위치를 바라보고 있을지를 결정

      // FutureBuilder 내의 future: checkPerimission() 실행 > 변경되는 점이 있으면 builder: (context)가 함수를 실행한다 >
      // checkPermission()을 실행한 결과를 snapshot에 return한다
      body: FutureBuilder(
          // future: future을 return 해주는 어떤 함수든 넣을 수 있다
          // 함수의 상태가 변경이 될 때마다 builder를 다시 실행해서 화면을 다시 그려준다, future 안에 들어간 함수가 return해준 값을 snapshot에서 받아볼 수 있다
          future: checkPermission(),
          // snapshot.connectionState 에서 connectionState는 ConnectionState 타입이며 none, waiting, done 값을 가지고 있다
          // snapshot.data는 futre에 있는 함수에서 return한 결과가 저장된다.

          builder: (BuildContext context, AsyncSnapshot snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return Center(
                child: CircularProgressIndicator(),
              );
            }

            // 위치 권환이 허가 됐을 때만 column(지도가 보이는 위젯)을 return 해줘야 한다
            if (snapshot.data == '위치 권한이 허가됐습니다.') {
              // 현재 위치가 변경될 떄마다 값이 stream에서 return build 된다
              // getPositionStream()을 통해 position클래스를 return 받을 수 있다
              return StreamBuilder<Position>(
                  stream: Geolocator.getPositionStream(),
                  builder: (context, snapshot) {
                    bool isWithinRange = false;
                    // 만약 데이터가 있으면
                    if (snapshot.hasData) {
                      final start = snapshot.data!; // 내 위치
                      final end = companyLatLng; // 회사 위치

                      final distance = Geolocator.distanceBetween(
                        start.latitude,
                        start.longitude,
                        end.latitude,
                        end.longitude,
                      );
                      // 회사와 디바이 거리가 100m안에 있으면
                      if (distance < okDistance) {
                        isWithinRange = true;
                      }
                    }
                    return Column(
                      children: [
                        _CustomGoogleMap(
                          initialPosition: initialPosition,
                          circle: choolCheckDone
                              ? checkDoneCircle
                              : isWithinRange
                                  ? withinDistanceCircle
                                  : notWithinDistanceCircle,
                          marker: marker,
                          onMapCreated: onMapCreated,
                        ),
                        _ChoolCheckButton(
                          isWithinRange: isWithinRange,
                          choolChekDone: choolCheckDone,
                          onPressed: onChoolCheckPressed,
                        ),
                      ],
                    );
                  });
            }
            // 거부했을 경우이다
            return Center(
              child: Text(snapshot.data),
            );
          }),
    );
  }

  onMapCreated(GoogleMapController controller) {
    mapController = controller;
  }

  onChoolCheckPressed() async {
    final result = await showDialog(
      // context는 stf에서는 어디서든 access가 가능
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: Text('출근하기'),
          content: Text('출근을 하시겠습니까'),
          actions: [
            TextButton(
              onPressed: () {
                // 취소버튼
                Navigator.of(context).pop(false);
              },
              child: Text('취소'),
            ),
            TextButton(
              onPressed: () {
                Navigator.of(context).pop(true);
              },
              child: Text('출근하기'),
            ),
          ],
        );
      },
    );

    if (result) {
      setState(() {
        choolCheckDone = true;
      });
    }
  }

  // 위치 권한 요청
  Future<String> checkPermission() async {
    // 앱과 상관없는 휴대폰 자체의 위치 활성화 기능을 사용할 수 있는가
    final isLocationEnabled = await Geolocator.isLocationServiceEnabled();

    if (!isLocationEnabled) {
      return '위치 서비스를 활성화 해주세요.';
    }
    // LocationPermission 이라는 형태로 Geolocator.checkPermission()은 현재 앱이 갖고 있는 위치 서비스에 대한 권한이 어떻게 되는지를 가져온다
    LocationPermission checkedPermission = await Geolocator.checkPermission();

    if (checkedPermission == LocationPermission.denied) {
      checkedPermission = await Geolocator.requestPermission();

      if (checkedPermission == LocationPermission.denied) {
        return '위치 권한을 허가해주세요';
      }
    }

    if (checkedPermission == LocationPermission.denied) {
      return '앱의 위치 권한을 세팅해서 허가해주세요.';
    }

    return '위치 권한이 허가됐습니다.';
  }

  AppBar renderAppBar() {
    return AppBar(
      title: Center(
        child: Text(
          '오늘도 출근',
          style: TextStyle(
            color: Colors.blue,
            fontWeight: FontWeight.w700,
          ),
        ),
      ),
      backgroundColor: Colors.white,
      actions: [
        IconButton(
          onPressed: () async {
            if (mapController == null) {
              return;
            }

            final location = await Geolocator.getCurrentPosition();

            mapController!.animateCamera(
              CameraUpdate.newLatLng(
                LatLng(
                  location.latitude,
                  location.longitude,
                ),
              ),
            );
          },
          color: Colors.blue,
          icon: Icon(
            Icons.my_location,
          ),
        )
      ],
    );
  }
}

class _CustomGoogleMap extends StatelessWidget {
  final CameraPosition initialPosition;
  final Circle circle;
  final Marker marker;
  final MapCreatedCallback onMapCreated;

  const _CustomGoogleMap(
      {required this.initialPosition,
      required this.circle,
      required this.marker,
      required this.onMapCreated,
      Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(
        flex: 2,
        child: GoogleMap(
          mapType: MapType.normal,
          initialCameraPosition: initialPosition,
          // 자기 위치 표시
          myLocationEnabled: true,
          // 내 위치로 가기 버튼
          myLocationButtonEnabled: false,
          circles: Set.from([circle]),
          // 가운데를 표시하는 marker
          markers: Set.from([marker]),
          onMapCreated: onMapCreated,
        ));
  }
}

class _ChoolCheckButton extends StatelessWidget {
  final bool isWithinRange;
  final VoidCallback onPressed;
  final bool choolChekDone;

  const _ChoolCheckButton(
      {required this.isWithinRange,
      required this.onPressed,
      required this.choolChekDone,
      Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Expanded(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Icon(
            Icons.timelapse_outlined,
            size: 50.0,
            color: choolChekDone
                ? Colors.green
                : isWithinRange
                    ? Colors.blue
                    : Colors.red,
          ),
          SizedBox(
            height: 20.0,
          ),
          // 이렇게 바로 if 쓸 수 있다. false이면 밑에 textbutton이 실행이 안 됨
          // 출첵이 안 돼있고 범위 안에 들어왔을 때
          if (!choolChekDone && isWithinRange)
            TextButton(
              onPressed: onPressed,
              child: Text('출근완료'),
            )
        ],
      ),
    );
  }
}
