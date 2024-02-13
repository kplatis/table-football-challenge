import { Button, Group, Select, SimpleGrid } from '@mantine/core'
import { useForm } from '@mantine/form'
import {
  validateFirstTeam,
  validateSecondTeam,
} from '../PlayedGameCreationForm/validation'
import { Team } from '@/types/teams'

type Props = {
  teams: Team[]
  setTeamsFn: (firstTeamId: number, secondTeamId: number) => void
}

export default function TeamSelectionForm({ teams, setTeamsFn }: Props) {
  const form = useForm({
    initialValues: {
      firstTeamId: null,
      secondTeamId: null,
    },
    validate: {
      firstTeamId: validateFirstTeam,
      secondTeamId: validateSecondTeam,
    },
  })

  const submit = (values: any) => {
    setTeamsFn(parseInt(values.firstTeamId), parseInt(values.secondTeamId))
  }

  const teamsData = teams.map((team) => ({
    value: team.id.toString(),
    label: team.name,
  }))

  return (
    <>
      <form onSubmit={form.onSubmit(submit)}>
        <SimpleGrid cols={2}>
          <Select
            label="First Team"
            name="firstTeamId"
            placeholder="Pick a team"
            data={teamsData}
            required={true}
            {...form.getInputProps('firstTeamId')}
          />

          <Select
            label="Second Team"
            name="secondTeamId"
            placeholder="Pick a team"
            data={teamsData}
            required={true}
            {...form.getInputProps('secondTeamId')}
          />
        </SimpleGrid>
        <Group justify="center" mt="md">
          <Button type="submit" size="md">
            Start the game!
          </Button>
        </Group>
      </form>
    </>
  )
}
