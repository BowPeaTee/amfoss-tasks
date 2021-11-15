import 'package:flutter/material.dart';
import 'package:introduction_screen/introduction_screen.dart';
import 'package:dots_indicator/dots_indicator.dart';
void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Intro()
    );
  }
}

class Intro extends StatelessWidget {
  Intro({Key? key}) : super(key: key);
  void _onIntroEnd(context) {
    Navigator.of(context).push(
      MaterialPageRoute(builder: (_) => const WelcomeScreen()),
    );
  }
  final pageDecoration = PageDecoration(
      titleTextStyle: const PageDecoration().titleTextStyle.copyWith(color: Colors.black),
      bodyTextStyle: const PageDecoration().bodyTextStyle.copyWith(color: Colors.black));
  List<PageViewModel> getPages() {
    return [
      PageViewModel(
          title: 'YOGA SURGE',
          image: Image.network("https://github.com/amfoss/tasks/raw/main/task-6/resources/page1.png"),
          body: 'Welcome to yoga world',
          footer: const Text('Inhale the future, exhale the past'),
          decoration: pageDecoration),

      PageViewModel(
          title: 'Healthy Freaks Exercises',
          image: Image.network("https://github.com/amfoss/tasks/raw/main/task-6/resources/page2.png"),
          body: 'Letting go is the hardest asana',
          decoration: pageDecoration),
      PageViewModel(
          title: 'Cycling',
          image: Image.network("https://github.com/amfoss/tasks/raw/main/task-6/resources/page3.png"),
          body: 'You cannot always control what goes on the outside. But you can control what goes on the inside',
          decoration: pageDecoration),
      PageViewModel(
          title: 'Meditation',
          image: Image.network("https://github.com/amfoss/tasks/raw/main/task-6/resources/page4.png"),
          body: 'The longest journey of any person is the journey inward',
          decoration: pageDecoration),
    ];
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: IntroductionScreen(
        globalBackgroundColor: const Color(0xffd6cbc7),
        pages: getPages(),
        showSkipButton: true,
        done: const Text(
          "Get Started",
          style: TextStyle(color: Colors.black),
        ),
        onDone: () => _onIntroEnd(context),
        skip: const Text("Skip", style: TextStyle(color: Colors.black)),
        dotsDecorator: getDotDecoration(),
      ),
    );
  }
  DotsDecorator getDotDecoration() => DotsDecorator(
    color: const Color(0xFFBDBDBD),
    //activeColor: Colors.orange,
    size: const Size(10, 10),
    activeSize: const Size(22, 10),
    activeColor: const Color(0xff2A2B32),
    activeShape: RoundedRectangleBorder(
      borderRadius: BorderRadius.circular(50),
    ),
  );
}

class WelcomeScreen extends StatelessWidget {
  const WelcomeScreen({Key? key}) : super(key: key);
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xffFAFAFA),
      appBar: AppBar(title: const Text('Welcome'),backgroundColor:const Color(0xFFD6CBC7)),
      body: Center(
        child: Column(
          children: <Widget>[
            Image.network('https://github.com/amfoss/tasks/raw/main/task-6/resources/welcome.png'),
            const Text("Mohith", style: TextStyle(fontSize: 35, fontWeight: FontWeight.bold)),
            const Text("Confused")
          ],
        ),
      ),
    );
  }
}