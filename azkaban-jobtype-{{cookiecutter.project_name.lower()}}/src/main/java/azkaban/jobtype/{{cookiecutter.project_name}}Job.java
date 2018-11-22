package azkaban.jobtype;

import azkaban.jobExecutor.AbstractJob;
import azkaban.utils.Props;
import azkaban.utils.PropsUtils;
import org.apache.log4j.Logger;

public class {{cookiecutter.project_name}}Job extends AbstractJob {


    protected volatile Props jobProps;
    protected volatile Props sysProps;

    public {{cookiecutter.project_name}}Job(final String jobId, final Props sysProps, final Props jobProps, final Logger log) {
        super(jobId, log);

        this.jobProps = jobProps;
        this.sysProps = sysProps;
    }

    @Override
    public void run() {
        resolveProps();

    }

    protected void resolveProps() {
        this.jobProps = PropsUtils.resolveProps(this.jobProps);
    }
}
