#include "func.h"
#include <ctime>
#include <fstream>
using namespace std;

namespace la {
    void increaseAndWriteRunNumber(const string& filename) {
        ifstream infile(filename);
        int currentRunNumber = 0;

        if (infile) {
            infile >> currentRunNumber;
        }

        infile.close();

        currentRunNumber++;

        ofstream outfile(filename);
        outfile << currentRunNumber << "-";
        outfile.close();

    }

    void writeCurrentTime(const string& filename) {
        time_t now = time(0);
        tm* timeinfo = localtime(&now);

        ofstream outfile(filename, ios_base::app);  
    
        outfile << 1900 + timeinfo->tm_year << "-"
            << 1 + timeinfo->tm_mon << "-"
            << timeinfo->tm_mday << "-"
            << timeinfo->tm_hour << "-"
            << timeinfo->tm_min << "-"
            << timeinfo->tm_sec;
        outfile.close();
    }
}