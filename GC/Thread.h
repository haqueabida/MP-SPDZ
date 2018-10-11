/*
 * Thread.h
 *
 */

#ifndef GC_THREAD_H_
#define GC_THREAD_H_

#include "Networking/Player.h"
#include "Tools/random.h"
#include "Processor.h"

namespace GC
{

struct ScheduleItem
{
    int tape;
    int arg;
    ScheduleItem(int tape = 0, int arg = 0) : tape(tape), arg(arg) {}
};

template<class T>
class Thread
{
    thread_local static Thread* singleton;

    static void* run_thread(void* thread);

public:
    Machine<T>& machine;
    Processor<T> processor;
    typename T::MC MC;
    Names& N;
    Player* P;
    PRNG secure_prng;
    vector<octetStream> os;

    int thread_num;
    WaitQueue<ScheduleItem> tape_schedule;
    WaitQueue<int> done;
    pthread_t thread;

    static Thread<T>& s();

    Thread(int thread_num, Machine<T>& machine, Names& N);
    virtual ~Thread();

    void run();
    virtual void pre_run() {}
    virtual void run(Program<T>& program);
    virtual void post_run() {}

    void join_tape();
    void finish();
};

template<class T>
thread_local Thread<T>* Thread<T>::singleton = 0;

template<class T>
Thread<T>& Thread<T>::s()
{
    if (singleton)
        return *singleton;
    else
        throw runtime_error("no singleton");
}

} /* namespace GC */

#endif /* GC_THREAD_H_ */
