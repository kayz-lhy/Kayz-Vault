//
// Created by Kayz on 2023/5/11.
//

#ifndef LEARNING_TEST_H
#define LEARNING_TEST_H

#include <QWidget>


QT_BEGIN_NAMESPACE
namespace Ui { class test; }
QT_END_NAMESPACE

class test : public QWidget {
    Q_OBJECT

public:
    explicit test(QWidget *parent = nullptr);

    ~test() override;

private:
    Ui::test *ui;
};


#endif //LEARNING_TEST_H
