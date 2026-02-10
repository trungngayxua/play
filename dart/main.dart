// constructors

class Student {
  String? name;
  int? age;
  int? id;

  Student(int id) {
    this.id = id;
  }

  Student.stuName(String name) {
    this.name = name;
  }

}

void main() {
  Student s1 = Student.stuName('nhu con cc');
  print(s1.name);
}
